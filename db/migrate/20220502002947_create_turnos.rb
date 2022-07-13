class CreateTurnos < ActiveRecord::Migration[6.0]
  def change
    create_table :turnos do |t|
      t.datetime :datetime
      t.string :departure_address
      t.boolean :is_it_return
      t.integer :seats
      t.string :arrival_address

      t.timestamps
    end
  end
end
