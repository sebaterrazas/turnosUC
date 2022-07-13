# frozen_string_literal: true

require 'rails_helper'

RSpec.describe User, type: :model do
  let(:user) { create(:user) }
  let(:second_user) { create(:user) }

  it 'is valid with valid attributes' do
    expect(user).to be_valid
  end

  it 'is not valid without name' do
    user.username = nil
    expect(user).not_to be_valid
  end

  it 'is not valid with a name too long' do
    user.username = '123456789 123456789 123456'
    expect(user).not_to be_valid
  end

  it 'is not valid with a name too short' do
    user.username = 'a'
    expect(user).not_to be_valid
  end

  it 'is not valid without an email' do
    user.email = nil
    expect(user).not_to be_valid
  end

  it 'is not valid with a repeated email' do
    user.email = second_user.email
    expect(user).not_to be_valid
  end
end
