from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

TELEGRAM_TOKEN = "925701438:AAE___H4J2GZwkfEyKxOr-eBm0ok9qa7adA"
#  Baseado em https://www.wemystic.com.br/artigos/numerologia-do-nome-calcule-seu-numero-e-descubra-a-sua-personalidade/
#  Baseado em https://medium.com/@mdcg.dev/desenvolvendo-o-seu-primeiro-chatbot-no-telegram-com-python-a9ad787bdf6


def start(bot, update):
    response_message = "=^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def numer(bot, update, args):
    nome_completo = str(update.message.from_user.first_name + " " + update.message.from_user.last_name)
    # tamanho_do_nome = len(nome_completo)

    soma_interior, soma_exterior, sintese, valor_atual = 0, 0, 0, 0

    for x in nome_completo:
        if x in ['a', 'j', 's']:
            valor_atual = 1
        if x in ['b', 'k', 't']:
            valor_atual = 2
        if x in ['c', 'l', 'u']:
            valor_atual = 3
        if x in ['d', 'm', 'v']:
            valor_atual = 4
        if x in ['e', 'n', 'w']:
            valor_atual = 5
        if x in ['f', 'o', 'x']:
            valor_atual = 6
        if x in ['g', 'p', 'y']:
            valor_atual = 7
        if x in ['h', 'q', 'z']:
            valor_atual = 8
        if x in ['i', 'r']:
            valor_atual = 9

        sintese += valor_atual
        vogais = ['a', 'e', 'i', 'o', 'u']
        if x in vogais:
            soma_interior += valor_atual
        else:
            soma_exterior += valor_atual

    aux_soma = 0
    while (sintese >= 10 and sintese != 11 and sintese != 22):
        for x in str(sintese):
            aux_soma += int(x)
        sintese = aux_soma

    aux_soma = 0
    while (soma_interior >= 10 and soma_interior != 11 and soma_interior != 22):
        for x in str(soma_interior):
            aux_soma += int(x)
        soma_interior = aux_soma

    aux_soma = 0
    while (soma_exterior >= 10 and soma_exterior != 11 and soma_exterior != 22):
        for x in str(soma_exterior):
            aux_soma += int(x)
        soma_exterior = aux_soma

    int_interior = ""
    int_exterior = ""
    int_sintese = ""

    if soma_interior == 1:
        int_interior = "Preza pela sua individualidade e independência, é um líder nato e tende a querer comandar as suas relações."
    if soma_interior == 2:
        int_interior = "É uma pessoa muito sensível, prefere ser comandado a comandar, é dependente emocionalmente das pessoas que ama."
    if soma_interior == 3:
        int_interior = "Tem o temperamento leve e alegre. Muito criativo, tem características infantis, o que pode ser positivo e também negativo."
    if soma_interior == 4:
        int_interior = "São pessoas que gostam de confiança, de tradição, de coisas previsíveis que estejam em seu controle. Busca relacionamentos sérios e estáveis."
    if soma_interior == 5:
        int_interior = "Adora novidades, aventuras, situações imprevisíveis. É sensual por natureza e não gosta de seguir tradições."
    if soma_interior == 6:
        int_interior = "São pessoas muito emotivas, apaixonadas e também ciumentas. Valoriza muito a família."
    if soma_interior == 7:
        int_interior = "São pessoas racionais que valorizam o conhecimento e a sabedoria. Ao mesmo tempo, tem lado espiritual elevado. Gosta de estar sozinho."
    if soma_interior == 8:
        int_interior = "Pragmático, justo, objetivo, parece dominar, mas é ultra-sensível."
    if soma_interior == 9:
        int_interior = "É agitado, cheio de energia, adora o movimento, foge da rotina. Gosta de investir em grandes planos e é muito ansioso."
    if soma_interior == 11:
        int_interior = "São pessoas transcendentais, é difícil conseguir compreendê-los por completo pois como são pessoas dotadas de muitas sabedorias diferentes, tem comportamento diverso, é uma caixinha de surpresas."
    if soma_interior == 22:
        int_interior = "São pessoas emocionalmente delicadas que se voltam à realização de ações em benefício do próximo e do mundo, mesmo que pareça impossível."

    if soma_exterior == 1:
        int_exterior = "Como gostam de liderar, parecem muito arrogantes e autoritários, mas na verdade ele só gosta de direcionar, aceita as opiniões alheias, por mais que lhe custe."
    if soma_exterior == 2:
        int_exterior = "Reflete o ambiente em que se encontra: se o ambiente é tenso, torna-se uma pessoa tensa, estressada. Se o ambiente é cheio de energia positiva, consegue multiplicá-la, etc."
    if soma_exterior == 3:
        int_exterior = "É uma pessoa muito simpática, se dá bem com todos, muito comunicativo. Até demais, as vezes fala tanto que parece um exibido."
    if soma_exterior == 4:
        int_exterior = "São pessoas que transmitem confiança no primeiro olhar. São sérios, determinados e respeitadores."
    if soma_exterior == 5:
        int_exterior = "É rebelde, provocativo e irônico. São muito sensuais e atraentes de forma peculiar."
    if soma_exterior == 6:
        int_exterior = "São pessoas que parecem ser da família, muito amorosos, próximos, transmitem hospitalidade."
    if soma_exterior == 7:
        int_exterior = "São inteligentes e peculiares, passa a ideia de ser “cheio de mania”, uma pessoa fria."
    if soma_exterior == 8:
        int_exterior = "Pessoas justas e objetivas em suas metas. Não tem rodeios."
    if soma_exterior == 9:
        int_exterior = "Se dá bem com todos ao redor apesar de ser impaciente e ansioso."
    if soma_exterior == 11:
        int_exterior = "Transmite um ar de mistério e parece inatingível ou incompreensível."
    if soma_exterior == 22:
        int_exterior = "São pessoas que parecem estar prontos para enfrentar qualquer situação na vida, tamanha sabedoria para lidar com as questões complicadas."

    if sintese == 1:
        int_sintese = "Uma pessoa que guia os outros e os representa."
    if sintese == 2:
        int_sintese = "Uma pessoa que facilita e colabora."
    if sintese == 3:
        int_sintese = "Uma pessoa que alegre, diverte,torna o ambiente leve."
    if sintese == 4:
        int_sintese = "Uma pessoa que se responsabiliza e cumpre os objetivos."
    if sintese == 5:
        int_sintese = "Uma pessoa que rompe as regras, questiona, se rebela."
    if sintese == 6:
        int_sintese = "Uma pessoa que mantém as tradições e a família em primeiro lugar."
    if sintese == 7:
        int_sintese = "Uma pessoa que analisa de maneira científica e busca os detalhes."
    if sintese == 8:
        int_sintese = "Uma pessoa  que promove a justiça e a prosperidade."
    if sintese == 9:
        int_sintese = "Uma pessoa que busca expandir e ultrapassar todos os seus limites."
    if sintese == 11:
        int_sintese = "Uma pessoa que não se encaixa em nenhum grupo específico."
    if sintese == 22:
        int_sintese = "Uma pessoa que quer realizar o impossível, custe o que custar."
    


    response_message = "{}, sua soma interior é {}, sua soma exterior é {}, e sua síntese é {}. \n\nA interpretação da soma interior é '{}'. \n\nDa soma exterior é '{}'. \n\nE sua síntese é '{}'.".format(nome_completo,soma_interior, soma_exterior, sintese, int_interior, int_exterior, int_sintese)

    # print(response_message)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def unknown(bot, update):
    response_message = "Meow? =^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler( CommandHandler('start', start) )
    dispatcher.add_handler( CommandHandler('numer', numer, pass_args=True) )
    dispatcher.add_handler( MessageHandler(Filters.command, unknown) )

    updater.start_polling()

    updater.idle()

    start


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
