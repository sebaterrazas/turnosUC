# frozen_string_literal: true

class ApplicationController < ActionController::Base
  before_action :set_page

  def set_page
    if current_user
      @requests_notification = (current_user.requests.where(state: %w[Accepted
                                                                      Rejected]) + current_user.recieved_requests.where(state: 'Pending')).sort_by(&:updated_at).reverse
      @turnos_notification = current_user.participating_turnos(as_driver = false).select do |t|
        %w[Finished Travelling].include?(t.status)
      end.sort_by(&:updated_at).reverse
    end
  end
end
