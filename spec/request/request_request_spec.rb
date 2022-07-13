# frozen_string_literal: true

require 'rails_helper'
require 'faker'

class RequestTest < ActiveSupport::TestCase
  RSpec.describe 'Requests', type: :request do
    let!(:requester) { create(:user) }
    let!(:turno) { create(:turno) }
    let!(:request) { create(:request) }

    let!(:attr_request) { { state: 'Pending', description: 'yrhtgrfe', user_id: requester.id, turno_id: turno.id } }
    let!(:invalid_attr_request) { { state: 'procesando', description: 'yrhtgrfe', turno_id: turno.id, user_id: requester.id } }

    describe 'get_index' do
      it 'should return a succesfull request' do
        get '/requests/'
        expect(response).to have_http_status(:found)
      end
    end

    describe 'post_new' do
      it 'should return a successful request' do
        sign_in requester
        post '/requests/', params: { request: attr_request }
        expect(response).to have_http_status(302)
      end
    end

    describe 'get_accept' do
      it 'should redirect' do
        sign_in requester
        patch "/requests/accept/#{request.id}"
        expect(response).to have_http_status(302)
      end
    end

    describe 'get_reject' do
      it 'should redirect' do
        sign_in requester
        patch "/requests/reject/#{request.id}"
        expect(response).to have_http_status(302)
      end
    end

    describe 'update' do
      it 'should change a Request' do
        expect do
          sign_in requester
          patch '/requests/edit', params: { request: { description: 'yrhtgr09sakjo0fe', id: request.id }, id: request.id }
          request.reload
        end.to change(request, :description)
      end
    end

    describe 'create' do
      it 'should increase count of Requests by 1' do
        expect do
          sign_in requester
          post '/requests', params: { request: attr_request }
        end.to change(Request, :count).by(1)
      end
      it 'should not increase count of Requests' do
        expect do
          sign_in requester
          post '/requests', params: { request: invalid_attr_request }
        end.to change(Request, :count).by(0)
      end
    end

    describe 'get_show' do
      it 'should return a successful request' do
        sign_in requester
        get '/requests/', params: { id: request.id }
        expect(response).to have_http_status(:ok)
      end
    end

    describe 'delete' do
      it 'should decrease count of Requests by 1' do
        expect do
          sign_in requester
          delete "/requests/#{request.id}"
        end.to change(Request, :count).by(-1)
      end
    end
  end
end
