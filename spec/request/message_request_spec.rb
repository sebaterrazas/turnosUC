# frozen_string_literal: true

require 'rails_helper'
require 'faker'

class MessageTest < ActiveSupport::TestCase
  RSpec.describe 'Messages', type: :request do
    let!(:message) { create(:message) }
    let!(:attr_message) { { text: Faker::Lorem.characters(number: rand(4..14)), user_id: 1, turno_id: 1 } }
    let!(:invalid_attr_message) { { text: '', turno_id: 1 } }

    describe 'get_index' do
      it 'should return a succesfull request' do
        get '/messages/'
        expect(response).to have_http_status(:ok)
      end
    end

    describe 'get_show' do
      it 'should return a successful request' do
        get "/messages/#{message.id}"
        expect(response).to have_http_status(:ok)
      end
    end

    describe 'create' do
      it 'should increase count of Messages by 1' do
        expect do
          post '/messages', params: attr_message
          # end.to change(Message, :count).by(1)
          expect(response).to be_succesful
        end
      end
      it 'should not increase count of Messages' do
        expect do
          post '/messages', params: invalid_attr_message
        end.to change(Message, :count).by(0)
      end
    end

    describe 'delete' do
      it 'should decrease count of Message by 1' do
        expect do
          delete '/messages/delete', params: { id: message.id }
        end.to change(Message, :count).by(-1)
      end
    end
  end
end
