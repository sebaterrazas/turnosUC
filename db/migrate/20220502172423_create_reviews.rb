class CreateReviews < ActiveRecord::Migration[6.0]
  def change
    create_table :reviews do |t|
      t.float :qualification
      t.string :content

      t.timestamps
    end
  end
end
