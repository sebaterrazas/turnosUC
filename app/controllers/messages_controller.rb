# frozen_string_literal: true

class MessagesController < ApplicationController
  def index
    @messages = Message.all
  end

  def create
    @messages_params = params.permit(:text, :user_id, :turno_id)
    @message = Message.create(@messages_params)
    redirect_to turnos_show_path(id: params[:turno_id])
  end

  def delete
    @message = Message.find(params[:id])
    turno_id = @message.turno.id
    @message.destroy
    redirect_to turnos_show_path(id: turno_id), notice: 'Message deleted'
  end

  def show
    @message = Message.find(params[:id])
  end
end
