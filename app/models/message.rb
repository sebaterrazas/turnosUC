# frozen_string_literal: true

class Message < ApplicationRecord
  validates :text, length: { minimum: 1 }

  belongs_to :turno
  belongs_to :user
end
