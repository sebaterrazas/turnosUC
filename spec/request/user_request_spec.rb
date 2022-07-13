# frozen_string_literal: true

require 'rails_helper'

class UserTest < ActiveSupport::TestCase
  RSpec.describe 'Users', type: :request do
    before(:each) do
      @attr_valid = {
        username: 'Example',
        phone: '123456',
        address: 'Av random',
        email: 'hola@abc.com',
        password: '123456',
        password_confirmation: '123456'
      }
      @attr_invalid = {
        username: 'Example',
        phone: '123456',
        address: 'Av random',
        email: 'holaabc.com',
        password: '12',
        password_confirmation: '123456'
      }
    end

    describe 'create' do
      it 'should redirect after create a user' do
        expect do
          post '/', params: { user: @attr_valid }
        end.to change(User, :count).by(1)
      end
    end

    describe 'get_show' do
      it 'should return a successful request' do
        @user = User.create!(@attr_valid)
        get "/users/#{@user.id}"
        expect(response).to have_http_status(:ok)
      end
    end

    describe 'get_index' do
      it 'should return a succesfull request' do
        get '/users/'
        expect(response).to have_http_status(:ok)
      end

      it 'should filter the Users by name' do
        expect do
          get '/users/', params: { q: 'jos' }
          expect(response).to have_http_status(:ok)
        end
      end
    end
  end
end
