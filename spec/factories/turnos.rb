# frozen_string_literal: true

require 'faker'

FactoryBot.define do
  factory :turno do
    departure_address { 'Valle escondido' }
    arrival_address { 'San Joaquín' }
    datetime { Faker::Time.between(from: 2.days.ago, to: Time.now) }
    seats { 3 }
    association :driver, factory: :user
  end
end
