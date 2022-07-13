# frozen_string_literal: true

require 'faker'

FactoryBot.define do
  factory :user do
    username { Faker::Lorem.characters(number: rand(4..14)) }
    phone { Faker::Lorem.word }
    email { Faker::Internet.email }
    address { 'Campus Oriente' }
    password { 123_456 }
  end
end
