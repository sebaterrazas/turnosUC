# frozen_string_literal: true

require 'faker'

# Una factory nos permitirá crear de manera sencilla instancias de una clase con diferentes valores
# y sin la necesidad de que nosotros le asignemos los parámetros al momento de crearla.
FactoryBot.define do
  factory :request do
    name { 'josé' }
    trip { 1 }
    state { 'Pending' }
    description { 'yrhtgrfe' }
    association :requester, factory: :user
    association :turno, factory: :turno
  end
end
