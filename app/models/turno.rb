# frozen_string_literal: true

class Turno < ApplicationRecord
  validates :departure_address, length: { minimum: 3, maximum: 40, message: 'Dirección de partida entre 3 y 40 caracteres' }
  validates :arrival_address, length: { minimum: 3, maximum: 40, message: 'Dirección de llegada entre 3 y 40 caracteres' }
  validates :datetime, presence: { message: 'Ingrese fecha' }
  #  validates :seats, presence: { message: 'Ingrese asientos libres' }
  validates :seats, numericality: { greater_than_or_equal_to: 1, less_than_or_equal_to: 6, message: 'Nº de pasajeros debe ser entre 1 y 6' }
  belongs_to :driver, class_name: 'User', foreign_key: :user_id

  has_many :recieved_requests, dependent: :destroy, class_name: 'Request'
  # has_many :passengers, class_name: 'User', through: :requests

  has_many :messages, dependent: :destroy

  has_many :recieved_reviews, dependent: :destroy, class_name: 'Review'

  def start_time
    datetime
  end

  def passengers
    recieved_requests.where(state: 'Accepted').map(&:requester)
  end

  def full?
    seats == passengers.count
  end

  def period
    start_date = (datetime.to_time - 1.hours).to_datetime
    end_date = (datetime.to_time + 1.hours).to_datetime
    start_date..end_date
  end

  def validate_other_booking_overlap(user)
    other_bookings = user.participating_turnos.reject { |t| t.id == id }
    is_overlapping = other_bookings.any? do |other_booking|
      puts "Overlaps with #{other_booking.datetime.strftime('%d-%m-%Y %H:%M')}" if period.overlaps?(other_booking.period)
      period.overlaps?(other_booking.period)
    end
    errors.add(:datetime, :overlaps_with_other, message: 'Fecha ocupada') if is_overlapping
  end
end
