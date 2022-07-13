# frozen_string_literal: true

class TurnosController < ApplicationController
  before_action :authenticate_user!, except: %i[index]

  def index
    @all_turnos = Turno.all
    @filtered_turnos = Turno.all
    if params[:arrival_address] && (params[:arrival_address] != '')
      @filtered_turnos = @filtered_turnos.where('lower(arrival_address) like ?',
                                                "%#{params[:arrival_address].downcase}%")
    end
    if params[:departure_address] && (params[:departure_address] != '')
      @filtered_turnos = @filtered_turnos.where('lower(departure_address) like ?',
                                                "%#{params[:departure_address].downcase}%")
    end
    @filtered_turnos = @filtered_turnos.select { |t| t.datetime.to_date.to_s == params[:date].to_s } if params[:date] && (params[:date] != '')
    @filtered_turnos = @filtered_turnos.select { |t| t.datetime.strftime('%H:%M') == params[:time] } if params[:time] && (params[:time] != '')
    if params[:time] || params[:date]
      status = []
      status << params[:scheduled] if params[:scheduled]
      status << params[:travelling] if params[:travelling]
      status << params[:finished] if params[:finished]
    else
      status = %w[Scheduled Travelling Finished]
    end
    @filtered_turnos = @filtered_turnos.select { |t| status.include? t.status }
    @filtered_turnos = sortbydate(@filtered_turnos)
  end

  def show
    @turno = Turno.find(params[:id])
    @passengers = @turno.recieved_requests.where(state: 'Accepted').map(&:requester)
    @pending_requests = @turno.recieved_requests.where(state: 'Pending')
    @request = Request.new
  end

  def new
    @turno = Turno.new
  end

  def create
    @turno_params = params.require(:turno).permit(:datetime, :departure_address, :arrival_address, :is_it_return, :seats, :id, :status)
    @turno = Turno.new(@turno_params)
    @turno.driver = current_user
    @turno.status = 'Scheduled'
    @turno.validate_other_booking_overlap(current_user) if @turno.datetime
    if @turno.errors.empty? && @turno.save
      redirect_to turnos_index_path, notice: 'Turno creado correctamente'
    else
      msg = 'Turno no creado: '
      @turno.errors.each do |_attribute, message|
        msg += "  [ #{message} ]"
      end
      redirect_to turnos_new_path, notice: msg
    end
  end

  def edit
    if params[:format]
      id_ = params[:format].split('/')[1]
      @tipo = params[:format].split('/')[0]
      @turno = Turno.find(id_)
    else
      @turno = Turno.find(params[:id])
      @tipo = if @turno.is_it_return
                'vuelta'
              else
                'ida'
              end
    end
    @tipo_original = if @turno.is_it_return
                       'vuelta'
                     else
                       'ida'
                     end

    redirect_to root_path, alert: 'Sólo puedes editar tus turnos' unless current_user.turnos.include? @turno
  end

  def update
    @turno_new_params = params.require(:turno).permit(:datetime, :departure_address, :arrival_address, :is_it_return, :seats, :status, :id)
    @turno = Turno.find(@turno_new_params[:id])
    @turno_updated = Turno.new(@turno_new_params)

    @turno_updated.datetime = @turno.datetime if @turno_new_params[:datetime] == ''
    if @turno_new_params[:status] == 'Travelling'
      @turno.recieved_requests.where(state: 'Pending').each do |request|
        request.state = 'Rejected'
      end
    end
    if @turno_new_params[:status] == 'Scheduled'
      @turno_updated.validate_other_booking_overlap(current_user)
      @turno.passengers.each do |passenger|
        @turno_updated.validate_other_booking_overlap(passenger)
      end
    end

    if @turno_updated.errors.empty? && @turno.update(@turno_new_params)
      redirect_to turnos_show_path(@turno.id), notice: 'Turno actualizado correctamente'
    else
      msg = 'Turno no actualizado: '
      @turno_updated.errors.each do |_attribute, message|
        msg += "  [ #{message} ]"
      end
      @turno.errors.each do |_attribute, message|
        msg += "  [ #{message} ]"
      end
      redirect_to turnos_edit_path(id: @turno.id), notice: msg
    end
  end

  def delete
    @turno = Turno.find(params[:id])
    if @turno.destroy
      redirect_to turnos_index_path, notice: 'Turno borrado correctamente'
    else
      redirect_to turnos_index_path, notice: 'Ocurrió un error. Turno NO eliminado'
    end
  end

  def sortbydate(turnos)
    turnos.sort_by(&:datetime)
  end
end
