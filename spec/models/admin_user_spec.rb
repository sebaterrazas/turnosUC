# frozen_string_literal: true

require 'rails_helper'

RSpec.describe AdminUser, type: :model do
  let(:admin_user) { create(:admin_user) }

  it 'is valid with valid attributes' do
    expect(admin_user).to be_valid
  end
end
