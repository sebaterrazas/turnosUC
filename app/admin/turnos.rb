# frozen_string_literal: true

ActiveAdmin.register Turno do
  # See permitted parameters documentation:
  # https://github.com/activeadmin/activeadmin/blob/master/docs/2-resource-customization.md#setting-up-strong-parameters
  #
  # Uncomment all parameters which should be permitted for assignment
  #
  permit_params :datetime, :departure_address, :is_it_return, :seats, :arrival_address, :user_id, :status
  #
  # or
  #
  # permit_params do
  #   permitted = [:datetime, :departure_address, :is_it_return, :seats, :arrival_address, :user_id, :status]
  #   permitted << :other if params[:action] == 'create' && current_user.admin?
  #   permitted
  # end
end
