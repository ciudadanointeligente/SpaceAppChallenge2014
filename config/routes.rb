SpaceAppChallenge2014::Application.routes.draw do
  root to: "home#index"
  resources :logs

end
