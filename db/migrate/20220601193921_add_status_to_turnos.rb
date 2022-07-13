class AddStatusToTurnos < ActiveRecord::Migration[6.0]
  def change
    add_column :turnos, :status, :string
  end
end
