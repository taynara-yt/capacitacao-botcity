"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    # bot.browse("http://www.botcity.dev")

    # Implement here your logic...
    bot.execute(r"C:\Program Files (x86)\Programas RFB\Sicalc Auto Atendimento\SicalcAA.exe")
    
    if not bot.find( "popup-esclarecimento", matching=0.97, waiting_time=20000):
        not_found("popup-esclarecimento")
    bot.click_relative(271, 255)
    
    
    if not bot.find( "funcoes", matching=0.97, waiting_time=10000):
        not_found("funcoes")
    bot.click()
    
    
    if not bot.find( "preenchimento-darf", matching=0.97, waiting_time=10000):
      not_found("preenchimento-darf")
    bot.click()
    
    if not bot.find( "cod_receita", matching=0.97, waiting_time=10000):
        not_found("cod_receita")
    bot.click_relative(226, 15)
    
    bot.kb_type("5629")
    
    bot.tab() 

    bot.wait(2000)

    if not bot.find( "pa", matching=0.97, waiting_time=10000):
        not_found("pa")
    bot.click_relative(46, 31)

    bot.paste("310120")
    
    if not bot.find( "valor_reais", matching=0.97, waiting_time=10000):
        not_found("valor_reais")
    bot.click_relative(64, 31)
    
    bot.paste("10000")

    if not bot.find( "calcular", matching=0.97, waiting_time=10000):
        not_found("calcular")
    bot.click()
    
    if not bot.find( "botao_darf", matching=0.97, waiting_time=10000):
        not_found("botao_darf")
    bot.click()
   
  
    if not bot.find( "nome", matching=0.97, waiting_time=10000):
        not_found("nome")
    bot.click_relative(17, 32)

    bot.paste("Petrobras")

    if not bot.find( "telefone", matching=0.97, waiting_time=10000):
        not_found("telefone")
    bot.click_relative(-6, 33)

    bot.paste("1199991234")
    
    if not bot.find( "cnpj", matching=0.97, waiting_time=10000):
        not_found("cnpj")
    bot.click_relative(174, 9)

    bot.paste("33000167000101")
    
    if not bot.find( "referencia", matching=0.97, waiting_time=10000):
        not_found("referencia")
    bot.click_relative(162, 11)

    bot.paste("0")
    
    
    if not bot.find( "imprimir", matching=0.97, waiting_time=10000):
        not_found("imprimir")
    bot.click()
    
    if not bot.find( "saida_impressao", matching=0.97, waiting_time=10000):
        not_found("saida_impressao")
    bot.click_relative(176, 459)

    bot.paste(r"C:\Users\taysi\OneDrive\Área de Trabalho\DARF-teste.pdf")
    bot.enter()


   
    
    
    

    
    

    

    
    




    
    





    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()


