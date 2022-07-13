# frozen_string_literal: true

Rails.application.routes.draw do
  devise_for :admin_users, ActiveAdmin::Devise.config
  ActiveAdmin.routes(self)
  
  get 'reviews/new', to: 'reviews#new', as: 'reviews_new'
  delete 'reviews/delete', to: 'reviews#delete', as: 'reviews_delete'
  post '/reviews', to: 'reviews#create'


  post '/messages', to: 'messages#create', as: 'messages_create'
  delete 'messages/delete', to: 'messages#delete', as: 'messages_delete'

  get 'turnos/', to: 'turnos#index', as: 'turnos_index'
  get 'turnos/new', to: 'turnos#new', as: 'turnos_new'
  post 'turnos/', to: 'turnos#create'
  get 'turnos/create'
  get 'turnos/edit', to: 'turnos#edit', as: 'turnos_edit'
  patch 'turnos/edit', to: 'turnos#update', as: 'turnos_update'
  get 'turnos/:id', to: 'turnos#show', as: 'turnos_show'
  delete 'turnos/:id', to: 'turnos#delete', as: 'turnos_delete'

  patch  '/requests/accept/:id', to: 'requests#accept', as: 'requests_accept'
  patch  '/requests/reject/:id', to: 'requests#reject', as: 'requests_reject'
  delete '/requests/:id', to: 'requests#destroy', as: 'requests_delete'
  resources :requests

  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  root to: 'turnos#index'
  get 'test', to: 'homes#inicio'
  # get 'test2', to: 'homes#test2'

  ######### READ #########
  get 'users/', to: 'users#index', as: 'users_index'
  get 'users/:id', to: 'users#show', as: 'users_show'

  get 'admin/', to: 'admin#login', as: 'admin_login'

  ########

  devise_for :users, controllers: {
    sessions: 'users/sessions',
    registrations: 'users/registrations'
  },
                     path: '', path_names: {
                       sign_in: 'login',
                       sign_out: 'logout', sign_up: 'register'
                     }
end
