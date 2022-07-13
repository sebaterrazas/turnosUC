# frozen_string_literal: true

class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  validates :username, length: { minimum: 3, maximum: 25 }

  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable

  has_one_attached :profile_pic, dependent: :destroy
  has_many :turnos, dependent: :destroy
  has_many :recieved_reviews, through: :turnos, class_name: 'Review'
  has_many :written_reviews, class_name: 'Review', dependent: :destroy
  has_many :requests, dependent: :destroy
  has_many :recieved_requests, through: :turnos, class_name: 'Request'

  has_many :messages, dependent: :destroy

  def display_avatar
    if profile_pic.attached?
      profile_pic
    else
      'default_profile_pic.png'
    end
  end

  def participating_turnos(as_driver = true)
    if as_driver
      Turno.all.select { |t| t.passengers.include?(self) || t.driver == self }
    else
      Turno.all.select { |t| t.passengers.include?(self) }
    end
  end
end
