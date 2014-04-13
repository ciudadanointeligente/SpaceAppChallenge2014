SpaceAppChallenge2014::Application.routes.draw do
  resources :observations

  root to: "home#index"
  resources :logs

end
