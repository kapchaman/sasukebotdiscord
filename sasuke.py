import discord
import random
import datetime
from discord.ext import commands
from itertools import cycle
import discord, os
from discord.ext import commands, tasks

status = cycle(['.info', 'Terraria', 'Minecraft','Human Fall Flat','Clash Royale'])

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    change_status.start()
    print('Bot is successfully activated. ')



@tasks.loop(minutes = 1)
async def change_status():
    await client.change_presence(status = discord.Status.idle, activity=discord.Game(next(status)))



@client.event
async def on_member_join(member):
    print(f'{member} присоединилися к нам.')


@client.event
async def on_member_remove(member):
    print(f'{member} покинул сервер.')


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
async def salam(ctx):
    await ctx.send('Уалейкум салам! ')


@client.command()
async def bday(ctx):
    em = discord.Embed(title='Дни Рождения', description='Днюхи пацанов', colour=discord.Color.green())
    em.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    em.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    em.set_thumbnail(url='https://ichef.bbci.co.uk/news/1024/cpsprodpb/633B/production/_87130452_87130450.jpg')
    birthdays = ('Алихан - 25-го января,2007 года,\n '
                 'Ерсултан - 7-го февраля,2006 года,\n '
                 'Бекжан - 25-го января,2006 года,\n'
                 'Асылбек - 15-го ноября,2006 года, \n'
                 'Данчо - 1 июнь,2007 года\n')
    await ctx.send(embed=em)
    await ctx.send(birthdays)


@client.command()
async def jack(ctx, *, question):
    users = ['Алека', 'Бекжан', 'Ерсик', 'Данчо', 'Асылбек']
    await ctx.send(f'Вопрос: {question}\nОтвет: {random.choice(users)} отвечаю!')


@client.command()
async def ping(ctx):
    await ctx.send(f'Твой пинг в сервере - {round(client.latency * 1000)} ms')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def jutsu(ctx):
    jutsuList = [
        [
            'Катон:Дзюцу Огненного Шара',
            'Дзюцу Теневого Клонирования',
            'Дзюцу Водяного Дракона',
            'Дзюцу Высвобождения Земли',
            'Чидори:1000 птиц',
            'Расенсюрикен',
            'Расенган',
        ], [
            'https://thumbs.gfycat.com/ImpartialOblongLarva-size_restricted.gif',
            'https://pa1.narvii.com/6901/40b1bb31231926f3295edbf43fde0562f0c22474r1-500-281_hq.gif',
            'https://thumbs.gfycat.com/EqualDemandingBasenji-size_restricted.gif',
            'https://2img.net/h/fc08.deviantart.net/fs70/f/2013/033/5/3/kakashi_vs_pain__2__by_tsotne_senpai-d5tkr6c.gif',
            'https://thumbs.gfycat.com/UntidyHorribleAnteater-size_restricted.gif',
            'https://i.gifer.com/c21.gif',
            'https://steamuserimages-a.akamaihd.net/ugc/936066442812937507/C1A0DA778189FF29FEC67613FFF28CCBF74580DB/',
        ]
    ]
    randNum = random.randint(0, len(jutsuList[0]) - 1)
    randJutsu = [jutsuList[0][randNum], jutsuList[1][randNum]]
    author = ctx.message.author
    embed = discord.Embed(
        title=f'{author}, ты использовал {randJutsu[0]}!',
        color=discord.Colour.red()
    )
    embed.set_image(url=randJutsu[1])
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def time(ctx):
    emb = discord.Embed(title='Время', description='Текущее время по Капчагаю', colour=discord.Color.red(), url='https://www.timeserver.ru/cities/kz/almaty')

    emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    emb.set_thumbnail(url='https://previews.123rf.com/images/arturaliev/arturaliev1406/arturaliev140600018/29255885-trendy-minimalistic-clock-with-transparent-shadow-.jpg')
    now_date = datetime.datetime.now()

    emb.add_field(name='Time till nanoseconds', value='Time is : {}'.format(now_date))

    await ctx.send(embed=emb)


@client.command()
async def nick(ctx, *, question):
    varieties = ["Китайский шелекбас",
                 "Стервозный насвай",
                 'Лошок1337',
                 'Главарь геев',
                 'Чмошный осырак',
                 'Лохматый бомж',
                 "Лысый огурец",
                 "Мешок с навозом",
                 "Козел с перхотью",
                 "Арбузная тварь",
                 "Бешенный узбек",
                 "Элитный Таджик",
                 "Просто лох",
                 "Киберкотлета",
                 "У тебя че фантазии нету?Сам себе ник придумывай!",
                 "Виртуозный чеченец",
                 "Реактивный дебил",
                 "Паленый волк",
                 "Чмошникам ники не придумываю,сорян"]
    await ctx.send(f'Вопрос: {question}\nОтвет: {random.choice(varieties)}')


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ["Это точно.",
                 "Это решительно так.",
                 "Без сомнения.",
                 "Определенно да.",
                 "Ты можешь положиться на это.",
                 "Как я понимаю, да.",
                 "Наверняка.",
                 "Прогноз хороший.",
                 "Да.",
                 "Знаки указывают на да.",
                 "Ответ странный, попробуйте еще раз.",
                 "Спроси об этом потом.",
                 "Лучше не говорить тебе сейчас",
                 "Не могу предсказать сейчас.",
                 "Сконцентрируйся и спроси снова",
                 "Иди нафиг)",
                 "Мой ответ - нет.",
                 "Мой внутренний майнкрафтер говорит ,нет.",
                 "Перспектива не очень хорошая.",
                 "Очень сомнительно.",
                 "Скорее всего,нет.",
                 "Меня создал Алихан.Спроси у него, ок?",
                 "А че без моего предсказания не можешь,глупец?",
                 "Цумбедм"]
    await ctx.send(f'Вопрос: {question}\nОтвет: {random.choice(responses)}')


@client.command()
async def perc(ctx, *, question):
    v = random.randint(0,100)
    await ctx.send(f'Вопрос: {question}\nОтвет: На {v} процентов!')


@client.command()
async def openbox(ctx):
    openbox_embed = discord.Embed(title="Игра Ящик Бравл Старса", description='Если вам выпадут 2 одинаковых числа, значит вы выиграли. '
                                                                'Ну а если 3, то это тотальный выигрыш, иными словами - джекпот! ', colour=discord.Color.blue())

    openbox_embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    openbox_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    openbox_embed.set_thumbnail(url='https://brawlstars.info/wp-content/uploads/2019/12/mega-box-brawl-stars.jpg')
    a = str(random.randint(0, 9))
    b = str(random.randint(0, 9))
    c = str(random.randint(0, 9))
    abc = a+b+c
    super_rare = ['Карл', 'Дэррил', 'Пенни', 'Рико', 'Джеки']
    epic = ['Беа', 'Фрэнк', 'Пэм', 'Пайпер', 'Нани', 'Биби']
    mythic = ['Мортис', 'Тара', 'Джин', 'Макс', 'Мистер П.', 'Спраут',"Гэйл"]
    legendary = ['Ворон', 'Спайк', 'Леон', 'Сэнди',"Вольт"]
    if a == b and a != c and b != c or a == c and a != b and a != c:
        openbox_embed.add_field(name=abc, value='Вы выиграли, Ваш приз :')
        openbox_embed.add_field(name='Мои поздравления!', value=random.choice(super_rare))

    elif b == a and b != c and b != a or b == c and b != a and c != a:
        openbox_embed.add_field(name=abc, value='Вы выиграли, Ваш приз :')
        openbox_embed.add_field(name='Мои поздравления!', value=random.choice(epic))

    elif c == a and c != b and a != b or c == b and c != a and a != b:
        openbox_embed.add_field(name=abc, value='Вы выиграли, Ваш приз: ')
        openbox_embed.add_field(name='Мои поздравления!', value=random.choice(mythic))

    elif a == b == c:
        openbox_embed.add_field(name=abc, value='УХ ТЫ, ЛЕГАА! ТЕБЕ ВЫПАЛ :')
        openbox_embed.add_field(name='Мои поздравления!', value=random.choice(legendary))

    elif a != b != c:
        openbox_embed.add_field(name=abc, value='Ахахахах ,лошара, ничего не выбил!!!Попробуй снова,вдруг повезет?')

    await ctx.send(embed=openbox_embed)



@client.command()
async def info(ctx):
    gtg = discord.Embed(title = 'Здравствуй',description='Я - бот созданный Алиханом, Саске Учиха! Вот инструкция к моим способностям:', colour=discord.Color.red())
    

    gtg.set_thumbnail(url='https://img1.goodfon.ru/original/1955x1125/9/97/naruto-uchiha-sasuke-2093.jpg')
    

    gtg.add_field(name='.команды', value = 'Информация о моих коммандах')
    gtg.add_field(name='.правила', value= "Информация о правилах в сервере")
    gtg.add_field(name='.роли', value='Информация о ролях в сервере')

    await ctx.send(embed=gtg)


@client.command()
async def команды(ctx):
    await ctx.send('1).salam - техника приветствия \n 2).8ball - техника призыва великого предсказателя.Задай вопрос после этой команды и я отвечу тебе \n 3).ping - техника пинга.Напиши эту команду и я напишу твой пинг в сервере \n 4).nick - техника обидного прозвища.Напиши эту команду и я дам тебе смешное призвание \n 5).time - техника часов.Я напишу в чат точное время до наносекунд. \n 6).clear - техника удаления сообщений.Я удалю столько сообщений сколько ты захочешь \n 7).kick - Я кикну того чей ник ты напишешь \n 8).ban - Также как и кик,но обратно твой обидчик уже не вернется. Использовать в крайнем случае \n 9).bday - техника напоминания наших ДР. Я напишу в чат дни рождения пользователей в сервере \n 10).perc - техника рандомных процентов. Напиши ее и задай мне вопрос.Я отвечу тебе процентами \n 11).jack - техника рандомайзера имен пользователей.Говоря простыми словами ты можешь написать ее и задать вопрос "Кто лох?" и я отвечу тебе рандомом\n 12).openbox - команда над которой мой создатель трудился 2 дня. Напиши ее и я открою тебе виртуальный бокс из игры Brawl Stars \n 13).write - Чмошная техника.Напиши после нее любые слова в кавычках и я напишу то же, что и ты \n 14).pc - техника рандом-игры на пк. Я напишу в чат игру которую тебе следует поиграть на пк \n 15).mobile - техника рандом-игр на мобильные устройства.Похоже на .pc ,но тут уже на мобилки\n 16).скучно - сырая техника,которая поможет мне ответить тебе чем занятся,когда скучно!\n 17).info - техника информации обо мне. \n 18).img - техника прикольной фотки \n 19).сулифа - техника вызова игры сулифа. Таким образом можно узнать кто лучше? Я или ты! \n 20).jutsu - использование рандомной техники из мира Наруто \n 21).narunick - узнай кто ты из мира Наруто')


@client.command()
async def роли(ctx):
    await ctx.send('1)Самая высокая роль в чатах,которую можно достичь - Админ\n 2)Ниже по званию - Хокаге. Если ты стал Хокаге знай,что наша деревня ценит тебя \n 3)Еще ниже - Модератор.Эта роль может входить почти во все каналы и управлять ими,но став модератором вы должны помогать создателю сервера\n 4)Ниже по званию - Джонин.Может все что не может обычный участник. \n 5)Ниже - Защитник Деревни.Можно получить эту роль сделав что-то полезное для нашего сервера \n 6)Отступник - ее получают те кто много активничают,но не помогают в развитии серваку.\n 7)Чунин - роль получают те кто достаточно активные,чтобы иметь доступ к некоторым каналам\n 8)Генин - пользователь,который проявил себя в немногих вещах \n 9)Самая низшая роль - Участник.Это пользователь,которому есть куда расти')

@client.command()
async def правила(ctx):
    await ctx.send('По сути правил в серваке нет,но есть раздражающие вещи.\n Во-первых это спам.Прошу не спамить в чатах во время разговора.Если хотите спамить идите в #спам-канал  :rage: \n Во-вторых это срачи в чатах.Прошу не злится и не поливать говном ваших дорогих собеседников :relaxed:')

@client.command()
async def img(ctx):
    fuck = discord.Embed(title='Вот тебе фотка', description='Чекай', color=discord.Color.red())
    imgs = ['https://sun9-35.userapi.com/c845520/v845520333/14b525/Q_ea9ARiJ4Q.jpg?ava=1','https://pm1.narvii.com/7382/20f09eeea52c3b995a37bc05c6e576862914c935r1-900-900v2_hq.jpg','https://cdn.discordapp.com/attachments/737291480145592384/743892278002843648/IMG-20191214-WA0025.jpg','https://pbs.twimg.com/media/EL2NomWWwAAA-Ut.jpg','https://pbs.twimg.com/media/Dd3dWrZU0AASSh5.jpg','https://media.moddb.com/images/members/5/4183/4182072/ao_5f7.jpeg','https://steamuserimages-a.akamaihd.net/ugc/943959157655107004/076158E0EA1D747C1208EEE2F177C7661DED7AB4/?imw=512&amp;imh=566&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true','https://arhivach.ng/storage/2/12/21211cbe4ab785c6aa2e718458e40c47.jpg','https://yt3.ggpht.com/a/AATXAJwTsFuM3Vevw9R4gSjLr2aUGbL2Bu6Bg_Ezzg=s900-c-k-c0xffffffff-no-rj-mo','https://steamuserimages-a.akamaihd.net/ugc/796491634686458489/8C3BB8766E037E57A1208AA36CCC6EE764605DF7/?imw=512&amp;imh=563&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true','https://avatars.mds.yandex.net/get-pdb/2104476/3feacccd-3f54-43ac-ab35-fa3610624c49/s1200?webp=false','https://i.imgur.com/2cFlOhF.png','https://i.ytimg.com/vi/D3ubP-Ik0H4/maxresdefault.jpg','https://i.ytimg.com/vi/yTB2_BX-7Gc/maxresdefault.jpg','https://i.ytimg.com/vi/5n5wp7VBoaU/maxresdefault.jpg','https://thumbs.gfycat.com/SardonicColossalDeermouse-size_restricted.gif','https://sun9-33.userapi.com/c852120/v852120879/a7b8f/7Jrho7capvw.jpg','https://yt3.ggpht.com/a/AATXAJwBHbt9UZYoHl51FGg6LjfbOJxDLgNTLF04ji8Kuw=s900-c-k-c0xffffffff-no-rj-mo','https://pbs.twimg.com/media/DTwiRTUVAAAbdgv.jpg:large','https://i06.fotocdn.net/s121/2d7a6c02ca306679/user_l/2758055850.jpg','https://i09.fotocdn.net/s121/73ced2d4f0c9d79f/user_l/2762773882.jpg','https://yt3.ggpht.com/a/AATXAJxpFVfBgezOyS1joYVHQ7AT3Nm3wMi7FZs_VYMK=s900-c-k-c0xffffffff-no-rj-mo','https://sun9-41.userapi.com/c854128/v854128339/1de71f/AIzMrDrRxJ0.jpg','https://pbs.twimg.com/media/DqFaq8gXgAApxgv.jpg:large',"https://sun9-23.userapi.com/c831209/v831209952/659c/UxMKMM8OJFA.jpg"]
    
    fuck.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    fuck.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    fuck.set_image(url=random.choice(imgs))
    await ctx.send(embed=fuck)



@client.command()
async def pc(ctx, *,question):
    pcgames = ["CS:GO",
    "Майнкрафт",
    "SAMP", 
    "Call of Duty 4:Modern Warfare",
    "CS Source",
    "Half Life 2",
    "ШХД:Зима",
    "Spore",
    "Portal",
    "Left For Dead", 
    "CS 1.6", 
    "ARK:Survival", 
    "RAFT", 
    "S.T.A.L.K.E.R.", 
    "Need For Speed:Most Wanted", 
    "Borderlands", 
    " Ну, я даже не знаю что тебе предложить!Спроси еще раз", 
    "Half Life", 
    "Fortnite (Если потянет конечно)",
    " Overwatch", 
    "Посмотри топ игр в ютубе!Возможно, что-то найдешь.",
    "У тебя походу фантазии нет раз у меня спрашиваешь",
    "GTA 4",
    "Assasin's Creed",
    "Mafia 2",
    "Far Cry 3",
    "Call of Duty:Modern Warfare 2",
    "Battlefield 3",
    "Mass Effect",
    "Fallout 3",
    "Metro 2033",
    "Ведьмак 2",
    "Dishonored",
    "GTA:Vice City",
    "Mirror's Edge",
    "Crysis 2",
    "Dead Space",
    "Max Payne 3",
    "Prototype",
    "Dota 2",
    "Crysis",
    "Watch Dogs",
    "Need For Speed:Underground",
    "Assasin's Creed:Unity",
    "Mortal Kombat 9",
    "Mortal Kombat X",
    "Prototype 2",
    "Far Cry",
    "Resident Evil",
    "Blur",
    "FlatOut 2",
    "Red Dead Redemption",
    "GTA 3",
    "Watch Dogs 2",
    "Just Cause",
    "The Walking Dead",
    "The Sims 3",
    "Doom",
    "Portal 2",
    "FIFA 18",
    "Metro Exodus",
    "Resident Evil 2",
    "Apex Legends",
    "Far Cry 4",
    "BioShock",
    "Halo",
    "Wolfenstein",
    "Skyrim",
    "Ведьмак 3:Дикая Охота",
    "God of War",]
    await ctx.send(f'Вопрос: {question}\nОтвет: {random.choice(pcgames)}')

@client.command()
async def narunick(ctx):
    author = ctx.message.author
    nicks = [
        [
            'Саске Учиха',
            'Наруто Узумаки',
            'Какаши Хатаке',
            'Шукаку',
            'Мататаби',
            'Исобу',
            'Сон Гоку',
            'Кокуо',
            'Сайкен',
            'Чоумей',
            'Гьюки',
            'Курама',
            'Утаката',
            'Киллер Би',
            'Шикамару',
            'Гаара',
            'Канкуро',
            'Обито',
            'Нагато',
            'Яхико',
            'Итачи Учиха',
            'Мизуки(лох которого слили в первой серий))',
        ],
        [
            'https://i.mycdn.me/i?r=AyH4iRPQ2q0otWIFepML2LxRTZIjFiG9TdF5cv_ILddlIA',
            'https://i.mycdn.me/i?r=AEE-HZfz734vGAKlsp5gLh-pzYvw2IEevQFxcH3H51diMbURGVkuFHceo2N1Kj9BHAy1bTyOW9W6Vt50qmjzMAG-&fn=external_8',
            'https://ru.citaty.net/media/authors/hatake-kakashi.png',
            'https://vignette.wikia.nocookie.net/naruto/images/9/99/Shukaku.png/revision/latest?cb=20170627050140&path-prefix=ru',
            'https://vignette.wikia.nocookie.net/naruto/images/a/a7/Matatabi.png/revision/latest?cb=20171028121323&path-prefix=ru',
            'https://jut.su/uploads/heroes/1377441553_isobu.jpg',
            'https://vignette.wikia.nocookie.net/naruto/images/5/5e/Son_Goku.png/revision/latest?cb=20171023125945&path-prefix=ru',
            'https://vignette.wikia.nocookie.net/naruto/images/a/a3/Kokuo.png/revision/latest/scale-to-width-down/340?cb=20140817215510',
            'https://vignette.wikia.nocookie.net/naruto/images/5/58/Saiken.png/revision/latest?cb=20140211075946',
            'https://i.pinimg.com/originals/41/27/7e/41277ef3620d8bafe13fd7788fd3fdfd.jpg',
            'https://vignette.wikia.nocookie.net/naruto/images/d/d7/Gyuki.png/revision/latest?cb=20140817221249',
            'https://pbs.twimg.com/profile_images/1018662043329728513/bIOL7N8A.jpg',
            'https://vignette.wikia.nocookie.net/naruto/images/b/b0/Utakataa.png/revision/latest?cb=20181109175936&path-prefix=ru',
            'https://wallpaperscave.ru/images/original/18/01-15/anime-naruto-10223.jpg',
            'https://vignette.wikia.nocookie.net/naruto/images/4/44/Shikamaru_Part_I.png/revision/latest?cb=20180225131949&path-prefix=ru',
            'https://static.wixstatic.com/media/ebf6a7_6b287767dce34c6185a4444095abfaa9~mv2.png/v1/fill/w_530,h_497,al_c,q_85,usm_0.66_1.00_0.01/ebf6a7_6b287767dce34c6185a4444095abfaa9~mv2.webp',
            'https://lh3.googleusercontent.com/proxy/vEEWkZwYGDpKUlCZIqwSIP9eWkmLD2yGL0irWLEQL5DM8Dx4ZY-F2SdiQpSrAYDoh2iRnKdkghuvsZtjHILF7dDLaFrErnbTXR-RweREuS3Cqxy7dggARD9BIyCIvbx5MiM',
            'https://shikimori.one/system/characters/original/2910.jpg',
            'https://i.pinimg.com/originals/34/e9/57/34e9577706d8e27ba3a1aa588b1a7d47.png',
            'https://i.pinimg.com/originals/c1/ff/eb/c1ffeb360c36c34dddd5baa602ab86d2.png',
            'https://vignette.wikia.nocookie.net/naruto/images/b/bb/Itachi.png/revision/latest?cb=20150609133421&path-prefix=ru',
            'https://vignette.wikia.nocookie.net/naruto/images/9/9c/Mizuki.png/revision/latest/top-crop/width/360/height/450?cb=20170830111403&path-prefix=ru',
        ]
    ]
    randNum = random.randint(0, len(nicks[0]) - 1)
    randPers = [nicks[0][randNum], nicks[1][randNum]]
    embed = discord.Embed(
        title=f'{author},  твое имя в Наруто: {randPers[0]}!',
        color=discord.Colour.red(),
    )
    embed.set_image(url=randPers[1])
    await ctx.send(embed=embed)


@client.command()
async def сулифа(ctx, *, question):
    rps_embed = discord.Embed(title="Камень | Ножница | Бумага", description="Вы будете играть не с человеком, а со мной. Давайте-ка посмотрим, кто лучше, человек или бот, бугагашки!", colour=discord.Color.red())
    rps_embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    rps_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    rps_embed.set_thumbnail(url='https://miro.medium.com/max/1500/1*Aln4flo6dzW1hRV34PmTRg.jpeg')
    ropasc = ['✊', '✌', '✋']
    bot = random.choice(ropasc)

    if question == bot:
        rps_embed.add_field(name='Ваш выбор', value=question)
        rps_embed.add_field(name='Мой выбор', value=bot)
        rps_embed.add_field(name='Ничейка вышла', value='В следующий раз я вас обыграю')
    elif question == 'камень' and bot == '✊':
        rps_embed.add_field(name='Ваш выбор', value='✊')
        rps_embed.add_field(name='Мой выбор', value=bot)
        rps_embed.add_field(name='Ничейка вышла', value='В следующий раз я вас обыграю')
    elif question == 'бумага' and bot == '✋':
        rps_embed.add_field(name='Ваш выбор', value='✋')
        rps_embed.add_field(name='Мой выбор', value=bot)
        rps_embed.add_field(name='Ничейка вышла', value='В следующий раз я вас обыграю')
    elif question == 'ножницы' and bot == '✌':
        rps_embed.add_field(name='Ваш выбор', value='✌')
        rps_embed.add_field(name='Мой выбор', value=bot)
        rps_embed.add_field(name='Ничейка вышла', value='В следующий раз я вас обыграю')

    elif question == '✌' or question == 'ножницы' and bot == '✋':
        rps_embed.add_field(name='Твой выбор', value='✌')
        rps_embed.add_field(name='Мой выбор', value=bot)
        rps_embed.add_field(name='Твоя взяла', value='Никогда не нравилась эта игра ▼_▼')
    elif question == '✊' or question == 'камень' and bot == '✌':
        rps_embed.add_field(name='Твой выбор', value='✊')
        rps_embed.add_field(name='Мой выбор', value=bot)
        rps_embed.add_field(name='Твоя взяла', value='Никогда не нравилась эта игра ▼_▼')  
    elif question == '✋' or question == 'бумага' and bot == '✊':
        rps_embed.add_field(name='Твой Выбор', value='✋')
        rps_embed.add_field(name='Мой выбор', value=bot)
        rps_embed.add_field(name='Твоя взяла', value='Никогда не нравилась эта игра ▼_▼')

    elif bot == '✌' and question == '✋' or question == 'бумага':
        rps_embed.add_field(name='Твой Выбор', value='✋')
        rps_embed.add_field(name='Мой выбор', value=bot)
        rps_embed.add_field(name='Ееее Я выиграл', value='Впрочем, было изично >.<')
    elif bot == '✊' and question == '✌' or question == 'ножницы':
        rps_embed.add_field(name='Твой Выбор', value='✌')
        rps_embed.add_field(name='Мой выбор', value=bot)
        rps_embed.add_field(name='Ееее Я выиграл', value='Впрочем, было изично >.<')  
    elif bot == '✋' and question == '✊' or question == 'камень':
        rps_embed.add_field(name='Твой Выбор', value='✊')
        rps_embed.add_field(name='Мой выбор', value=bot)
        rps_embed.add_field(name='Ееее Я выиграл', value='Впрочем, было изично >.<')
    
    else:
        rps_embed.add_field(name='Ты тупой?', value=f'Не помню, чтобы в игре было такого 0_o! {question} серьезно???')

    await ctx.send(embed=rps_embed)


@client.command()
async def mobile(ctx , *,question):
    mobgames = [ "Mortal Kombat Mobile", 
    "Мафия Онлайн", 
    "Brawl Stars", 
    "GTA:San Andreas", 
    "FNAF(Любую часть)", 
    "Asphalt 9: Legends",
    "Clash of Clans", 
    "Minecraft:PE", 
    "Slither.io" ,
    "Agar.io", 
    "Clash Royale", 
    "King of Thieves", 
    "Standoff 2", 
    "Free Fire", 
    "PUBG Mobile", 
    "Lords Mobile", 
    "Beat Blade", 
    "RAID:Shadow Legends", 
    "Call of Duty: Mobile", 
    "CSR Racing 2", 
    "Real Racing 3", 
    "Terraria", 
    "Roblox", 
    "Cut the Rope", 
    "Plants VS Zombies", 
    "Pixel Art", 
    "Zombie Catchers", 
    "Subway Sufers", 
    "Drive Ahead!", 
    "Hungry Shark Evolution", 
    "Smash Hit", 
    "BADLAND", 
    "Angry Birds", 
    'Bowmasters', 
    "Ахахах че, компа нет?", 
    "Почему я должен искать игру для тебя?"
    "Тупойсынба?",
    "Shadow Fight 2",
    "Shadow Fight 3",
    "Fortnite",
    "PES 2020 Mobile",
    "Hello Neighbor",
    "Plague Inc.",
    "Soul Knight"]

    await ctx.send(f'Вопрос: {question}\nОтвет: {random.choice(mobgames)}')

@client.command(pass_context=True)
async def write(ctx, arg):
    await ctx.send(arg)

@client.command()
async def скучно(ctx):
    deals = ["Поиграй во что-то",
    "Посмотри фильм",
    "Посмотри аниме или мультфильм",
    "Займись спортом дома!",
    "Убери квартиру",
    "Учи иностранный язык",
    "Почитай Книгу/Комиксы/Мангу",
    "Учись Программированию",
    "Посмотри видосы в ютубе",
    "Послушай музыку",
    "Нарисуй что-либо",
    "Научись играть на каком-то инструменте",
    "Иди поспи",
    "Сделай что-то из категории Оригами",
    "Научись какому-то новому навыку",
    "Научись Флексить))" ]
    await ctx.send(f'Ответ: {random.choice(deals)}')

@client.command()
async def казах(ctx):
    await ctx.send("Красавчик!")


client.run('NzM3NTc1ODc3MjEwMTQ0Nzc4.Xx_XEA.XNCgBBeCkG5mbt6a18_c5Vsd3I')
