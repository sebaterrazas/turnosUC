# frozen_string_literal: true

class Request < ApplicationRecord
  validates :state, acceptance: { accept: %w[Pending Accepted Rejected] }

  belongs_to :turno
  belongs_to :requester, class_name: 'User', foreign_key: :user_id
end
