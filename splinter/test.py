from splinter import Browser

executable_path = { 'executable_path' : 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe' }

with Browser( 'chrome' , **executable_path) as browser:
        # Visit URL
        url = "http://localhost:8000/admin"
        browser.visit(url)
        #test login
        browser.fill( "username" , "admin" )
        browser.fill( "password" , "admin12345" )
        button = browser.find_by_xpath( '//*[@id="login-form"]/div[3]/input' )
        button.click()
        if browser.is_text_present( 'Django administration' ):
                print ( "Login: Success" )
        else:
                print ( "Login: Error" )
                
        browser.click_link_by_partial_href( '/admin/posts/usuario/add/' )
        browser.fill( "nombre" , "satoshi" )
        browser.fill( "usuario" , "satoshi" )
        browser.fill( "password" , "satoshi" )
        button = browser.find_by_xpath( '//*[@id="usuario_form"]/div/div/input[1]' )
        button.click()
        if browser.is_text_present( 'was added successfully' ):
                print ( "Create Usuario: Success" )
        else:
                print ( "Create Usuario: Error" )
                
        input ( 'Waiting a key...' )
