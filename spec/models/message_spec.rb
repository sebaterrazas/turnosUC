# frozen_string_literal: true

require 'rails_helper'

RSpec.describe Message, type: :model do
  # Todo lo que está dentro de este bloque se ejecutará una vez antes de cada it
  before(:each) do
    # Creamos una instancia de la clase publicación "a mano", sin una factory
    @message = Message.new(text: 'The text')
  end

  it 'is not valid with no text' do
    @message.text = nil
    expect(@message).not_to be_valid
  end
end
