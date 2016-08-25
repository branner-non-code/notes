## Things Learned, ActiveRecord (running list)

 1. Setting up ActiveRecord database
 
    2. Create database:
    
    ```ruby
    bundle exec rake db:create
    ````

    2. Update database from a migration file:

    ```ruby
    bundle exec rake db:migrate
    ```

    2. Generate migration template for a new database-table and corresponding class:

    ```ruby
    bundle exec rake generate:migration NAME=create_people
    ```
    
    2. Roll back a migration:

    ```ruby
    bundle exec rake db:rollback
    ```
    
    2. Run `rspec` tests as `bundle exec rspec spec...`

    2. Seed:

    ```ruby
    bundle exec rake db:seed
    ```

 1. Use Pry as Sinatra console. In `Rakefile` change
 
    ```ruby
    desc 'Start IRB with application environment loaded'                            
    task "console" do
      exec "irb -r ./config/environment"
    end
    ```
    
    to

    ```ruby
    desc 'Start Pry with application environment loaded'                            
    task "console" do
      exec "pry -r ./config/environment"
    end
    ```

    In addition, to `Gemfile` add line:
    
    ```ruby
    gem 'pry'
    ```
    
    TODO: move this to Ruby notes?

 1. Methods on objects:
    
       ```ruby
       count
       persisted?
       save
       create(<hash>)
       find_by(<attribute>)
       find_or_initialize_by(<attribute>) # does not save
       find_or_create_by(<attribute>) # saves after creating
       ```

---

### Already moved to Notes on line.

(None)

[end]
