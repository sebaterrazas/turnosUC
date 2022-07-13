# frozen_string_literal: true

require 'rails_helper'
require 'faker'

class TurnoTest < ActiveSupport::TestCase
  RSpec.describe 'Turnos', type: :request do
    let(:driver) { create(:user) }
    let!(:turno) { create(:turno) }
    let!(:attr_turno) do
      { departure_address: Faker::Lorem.characters(number: rand(4..14)), arrival_address: Faker::Lorem.characters(number: rand(4..14)),
        datetime: Faker::Time.between(from: 2.days.ago, to: Time.now), seats: 4, user_id: driver.id, status: 'Travelling' }
    end
    let!(:invalid_attr_turno) do
      { departure_address: Faker::Lorem.characters(number: rand(29..30)), arrival_address: Faker::Lorem.characters(number: rand(1..2)),
        datetime: Faker::Time.between(from: 2.days.ago, to: Time.now), seats: 7, user_id: driver.id }
    end

    describe 'create' do
      it 'should redirect after create a turno' do
        expect do
          sign_in driver
          post '/turnos/', params: { turno: turno.attributes }
          expect(response).to have_http_status(302)
        end
      end
    end

    describe 'get_index' do
      it 'should return a succesfull request' do
        sign_in driver
        get '/turnos/'
        expect(response).to have_http_status(:ok)
      end

      it 'should filter the Turno by departure address' do
        expect do
          sign_in driver
          get '/users', params: { q: turno.departure_address }
          expect(response).to have_http_status(:ok)
        end
      end
    end

    describe 'get_new' do
      it 'should return a successful request' do
        sign_in driver
        get '/turnos/new'
        expect(response).to have_http_status(200)
      end
    end

    describe 'post_new' do
      it 'should return a successful request' do
        sign_in driver
        post '/turnos/', params: { turno: attr_turno }
        expect(response).to have_http_status(302)
      end
    end

    describe 'create' do
      it 'should increase count of Turnos by 1' do
        expect do
          sign_in driver
          post '/turnos', params: { turno: attr_turno }
        end.to change(Turno, :count).by(1)
      end
      # Se pasan atributos invalidos y se ve que la cuenta de Publicaciones no cambie
      it 'should not increase count of Turnos' do
        expect do
          sign_in driver
          post '/turnos', params: { turno: invalid_attr_turno }
        end.to change(Turno, :count).by(0)
      end
    end

    describe 'get_edit' do
      it 'should return a successful request' do
        sign_in turno.driver
        get '/turnos/edit', params: { format: "#{turno.is_it_return}/#{turno.id}" }
        expect(response).to have_http_status(200)
      end
    end

    describe 'patch_edit' do
      it 'should return a successful request' do
        sign_in driver
        attr_turno_aux = attr_turno.clone
        attr_turno_aux[:id] = turno.id
        patch '/turnos/edit', params: { turno: attr_turno_aux }
        expect(response).to have_http_status(302)
      end
    end

    describe 'update' do
      it 'should change a Turno' do
        expect do
          sign_in driver
          patch '/turnos/edit', params: { turno: { arrival_address: 'Naboo', id: turno.id } }
          turno.reload
        end.to change(turno, :arrival_address)
      end
    end

    describe 'update' do
      it 'should not change a Turno' do
        expect do
          sign_in driver
          patch '/turnos/edit', params: { turno: { seats: 563, id: turno.id } }
          turno.reload
        end.to_not change(turno, :seats)
      end
    end

    describe 'get_show' do
      it 'should return a successful request' do
        sign_in driver
        get "/turnos/#{turno.id}"
        expect(response).to have_http_status(:ok)
      end
    end

    describe 'delete' do
      it 'should return a successful request' do
        sign_in driver
        delete "/turnos/#{turno.id}"
        expect(response).to have_http_status(302)
      end
    end

    describe 'delete' do
      it 'should decrease count of Turnos by 1' do
        expect do
          sign_in driver
          delete "/turnos/#{turno.id}"
        end.to change(Turno, :count).by(-1)
      end
    end
  end
end
