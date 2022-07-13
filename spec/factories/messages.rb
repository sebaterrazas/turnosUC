# frozen_string_literal: true

require 'faker'

# Una factory nos permitirá crear de manera sencilla instancias de una clase con diferentes valores
# y sin la necesidad de que nosotros le asignemos los parámetros al momento de crearla.
FactoryBot.define do
  factory :message do
    text { Faker::Lorem.paragraph }
    association :user, factory: :user
    association :turno, factory: :turno
  end
end
