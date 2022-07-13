class CreateRequests < ActiveRecord::Migration[6.0]
  def change
    create_table :requests do |t|
      t.string :name
      t.integer :trip
      t.string :state
      t.text :description

      t.timestamps
    end
  end
end
