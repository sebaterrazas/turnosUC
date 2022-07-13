# frozen_string_literal: true

class UsersController < ApplicationController
  def show
    @user = User.find(params[:id])
    @pending_requests = @user.requests.select { |r| r.state == 'Pending' && r.turno.status == 'Scheduled' }
    @nota_promedio = if @user.recieved_reviews.count.zero?
                       'Sin reseñas'
                     else
                       "#{(@user.recieved_reviews.map(&:qualification).sum / @user.recieved_reviews.count).round(1)} / 5"

                     end
  end

  def index
    @filtered_users = if params[:q]
                        User.where('lower(username) like ?', "%#{params[:q].downcase}%")
                      else
                        User.all
                      end
  end
end
