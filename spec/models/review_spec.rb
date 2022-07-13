# frozen_string_literal: true

require 'rails_helper'

RSpec.describe Review, type: :model do
  # Todo lo que está dentro de este bloque se ejecutará una vez antes de cada it
  before(:each) do
    # Creamos una instancia de la clase publicación "a mano", sin una factory
    @review = Review.new(qualification: 'A qualification', content: 'Content of the review')
  end

  it 'is not valid with no qualification' do
    @review.qualification = nil
    expect(@review).not_to be_valid
  end

  it 'is not valid with a qualification too short' do
    @review.qualification = 'a'
    expect(@review).not_to be_valid
  end

  it 'is not valid with no content' do
    @review.content = nil
    expect(@review).not_to be_valid
  end

  it 'is not valid with a content too short' do
    @review.content = 'asd'
    expect(@review).not_to be_valid
  end
end
