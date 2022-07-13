# frozen_string_literal: true

require 'rails_helper'

RSpec.describe Turno, type: :model do
  let(:driver) { create(:user) }
  let(:turno) { create(:turno) }

  it 'is valid with valid attributes' do
    expect(turno).to be_valid
  end

  it 'is not valid without datetime' do
    turno.datetime = nil
    expect(turno).not_to be_valid
  end

  it 'is not valid with a departure address too short' do
    turno.departure_address = 'a'
    expect(turno).not_to be_valid
  end

  it 'is not valid with a arrival address too short' do
    turno.arrival_address = 'a'
    expect(turno).not_to be_valid
  end

  it 'is not valid with a departure address too long' do
    turno.departure_address = '123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'
    expect(turno).not_to be_valid
  end

  it 'is not valid with a arrival address too long' do
    turno.arrival_address = '123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'
    expect(turno).not_to be_valid
  end

  it 'is not valid with less than 1 seats' do
    turno.seats = 0
    expect(turno).not_to be_valid
  end

  it 'is not valid with more than 6 seats' do
    turno.seats = 7
    expect(turno).not_to be_valid
  end
end
