# frozen_string_literal: true

class Review < ApplicationRecord
  validates :qualification, presence: { message: 'Ingrese una calificación' }

  belongs_to :turno
  belongs_to :reviewer, class_name: 'User', foreign_key: :user_id
end
