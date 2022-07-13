# frozen_string_literal: true

class RequestsController < ApplicationController
  before_action :set_request, only: %i[show edit update destroy]
  before_action :authenticate_user!

  # GET /requests or /requests.json
  def index
    @requests = Request.all
  end

  # GET /requests/1 or /requests/1.json
  def show; end

  # GET /requests/new
  def new
    @request = Request.new
  end

  # GET /requests/1/edit
  def edit; end

  # POST /requests or /requests.json
  def create
    @request = Request.new(request_params)
    @request.turno.validate_other_booking_overlap(@request.requester)
    if @request.turno.errors.empty? && @request.save
      redirect_to turnos_show_path(@request.turno_id), notice: 'Solicitud enviada'
    else
      msg = 'Solicitud no enviada: '
      @request.turno.errors.each do |_attribute, message|
        msg += "  [ #{message} ]"
      end
      @request.turno.errors.clear
      redirect_to turnos_show_path(id: @request.turno.id), notice: msg
    end
  end

  def accept
    @request = Request.find(params[:id])
    @request.state = 'Accepted'
    redirect_to turnos_show_path(@request.turno_id) if @request.save
  end

  def reject
    @request = Request.find(params[:id])
    @request.state = 'Rejected'
    @request.destroy
    redirect_to turnos_show_path(@request.turno_id)
  end

  # PATCH/PUT /requests/1 or /requests/1.json
  def update
    respond_to do |format|
      if @request.update(request_params)
        format.html { redirect_to request_url(@request), notice: 'Request was successfully updated.' }
        format.json { render :show, status: :ok, location: @request }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @request.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /requests/1 or /requests/1.json
  def destroy
    @request.destroy
    respond_to do |format|
      format.html { redirect_back fallback_location: '/', allow_other_host: false, notice: 'Haz salido correctamente del turno.' }
      format.json { head :no_content }
    end
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_request
    @request = if params[:id] == 'edit'
                 Request.find(params[:request][:id])
               else
                 Request.find(params[:id])
               end
  end

  # Only allow a list of trusted parameters through.
  def request_params
    params.require(:request).permit(:user_id, :state, :turno_id, :description)
  end
end
