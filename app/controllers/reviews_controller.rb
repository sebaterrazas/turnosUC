# frozen_string_literal: true

class ReviewsController < ApplicationController
  def edit; end

  def index
    @user = User.find(params[:user_id]) if params[:user_id]
  end

  def new
    @turno = Turno.find(params[:turno_id])
    @review = Review.new
  end

  def show
    @review = Review.find(params[:id])
  end

  def create
    @reviews_params = params.require(:review).permit(:qualification, :content, :reviewer, :turno, :user_id, :turno_id)
    @review = Review.create(@reviews_params)
    if @review.save
      redirect_to turnos_show_path(@review.turno_id), notice: 'Reseña creada correctamente'
    else
      msg = 'Reseña no creada: '
      @review.errors.each do |_attribute, message|
        msg += "  [  #{message}  ]"
      end
      redirect_to reviews_new_path(turno_id: @review.turno_id), notice: msg
    end
  end

  def delete
    @review = Review.find(params[:id])
    @review.destroy
    redirect_to reviews_index_path, notice: 'Review deleted'
  end
end
