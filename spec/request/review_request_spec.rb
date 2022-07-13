# frozen_string_literal: true

require 'rails_helper'
require 'faker'

class ReviewTest < ActiveSupport::TestCase
  RSpec.describe 'Reviews', type: :request do
    let!(:review) { create(:review) }
    let!(:turno) { create(:turno) }
    let!(:user) { create(:user) }

    let!(:attr_review) { { qualification: 6.9, content: Faker::Lorem.characters(number: rand(4..14)), user_id: user.id, turno_id: turno.id } }
    let!(:invalid_attr_review) { { qualification: 'holi', content: 'a' } }

    describe 'get_new' do
      it 'should return a successful request' do
        sign_in user
        get '/reviews/new', params: { turno_id: turno.id }
        expect(response).to have_http_status(200)
      end
    end

    describe 'get_show' do
      it 'should return a succesfull request' do
        get '/reviews/show', params: { id: review.id }
        expect(response).to have_http_status(:ok)
      end
    end

    describe 'get_index' do
      it 'should return a succesfull request' do
        get '/reviews/', params: { user_id: user.id }
        expect(response).to have_http_status(:ok)
      end
    end

    describe 'create' do
      it 'should increase count of Reviews by 1' do
        expect do
          post '/reviews', params: { review: attr_review }
        end.to change(Review, :count).by(1)
      end
      it 'should not increase count of Reviews' do
        expect do
          post '/reviews', params: { review: invalid_attr_review }
        end.to change(Review, :count).by(0)
      end
    end

    describe 'delete' do
      it 'should decrease count of Reviews by 1' do
        expect do
          delete '/reviews/delete', params: { id: review.id }
        end.to change(Review, :count).by(-1)
      end
    end
  end
end
