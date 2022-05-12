import os
from docxtpl import DocxTemplate, InlineImage
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

pas = input('Откуда брать данные:\n')
to_pas = input('\nКуда сохранять:\n')

df_code = pd.read_excel(f'{os.getcwd()}/КОДЫ.xlsx')
SRG = pd.read_excel(f'{os.getcwd()}/ЦРГ.xlsx')
adres_med = pd.read_excel(f'{os.getcwd()}/адреса учреждений.xlsx')

df_base = pd.read_csv(f'{pas}/выгрузка.csv', delimiter=';', low_memory=False)
base = pd.read_excel(f'{pas}/Журнал регистрации формы сведений о ребенке.xlsx')

base['дополнительная ЦРГ подгруппа №'] = base['ЦРГ подгруппа №']
base['ЦРГ подгруппа №'] = [str(i).split('.')[0] for i in base['ЦРГ подгруппа №']]


def get_df(SNILS):
    df = df_code.copy()
    result_2 = df_base.copy()

    index_list = [0, 1, 2, 3, 4, 5, 8, 12, 13, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
                  44, 45, 46, 47, 48, 49, 50, 52, 53, 56, 57, 58, 59, 60, 61, 62, 63,
                  66, 67, 68, 69, 70, 71, 72, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                  87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]
    for i in index_list: df['Значение'][i] = \
    result_2.loc[result_2['СНИЛС'] == SNILS, [df['Наименование'][i]]].values[0][0]

    df['Значение'][64] = df['Значение'][60].split('.')[1]

    df['Значение'][65] = base.loc[base['СНИЛС'] == SNILS, '№ п/п'].values[0]

    for i in [3, 39, 45, 50, 59, 62]: df['Значение'][i] = df['Значение'][i].split()[0]

    for i in [5, 8]: df['Значение'][df.loc[df['Наименование'] == df['Значение'][i]].index] = 'X'

    for i in [66, 67, 68, 69, 70, 71, 72]:
        if df['Значение'][i] == 'Не установлено':
            df.loc[i, 'Значение'] = ''
        else:
            df.loc[i, 'Значение'] = 'X'

    if df['Значение'][13] == 'Адрес места жительства':
        v = {16: 'обл', 17: 'р-н', 19: 'ул', 20: 'д', 21: 'корп', 23: 'кв'}
        x = df.loc[12, 'Значение'].split(', ')
        df.loc[15, 'Значение'] = x.pop(0)
        df.loc[14, 'Значение'] = 'Российская Федерация'
        for key, value in v.items():
            try:
                df.loc[key, 'Значение'] = x.pop(x.index(list(filter(lambda x: value in x, x))[0]))
            except:
                None
        if df.loc[19, 'Значение'] == '' and len(x) > 1: df['Значение'][19] = x.pop(len(x) - 1)
        df.loc[18, 'Значение'] = (', ').join(x)

    elif df['Значение'][13] == 'Адрес места постоянной регистрации':
        df['Значение'][24] = 'Российская Федерация'
        v = {26: 'обл', 27: 'р-н', 29: 'ул', 30: 'д', 31: 'корп', 33: 'кв'}
        x = df['Значение'][12].split(', ')
        df['Значение'][25] = x.pop(0)
        for key, value in v.items():
            try:
                df['Значение'][key] = x.pop(x.index(list(filter(lambda x: value in x, x))[0]))
            except:
                None
        if df['Значение'][29] == '' and len(x) > 1: df['Значение'][19] = x.pop(len(x) - 1)
        df['Значение'][28] = (', ').join(x)

    # Прописывание значений ЦРГ
    df.loc[73, 'Значение'] = base.loc[base['СНИЛС'] == SNILS, 'ЦРГ подгруппа №'].values[0]
    df.loc[74, 'Значение'] = SRG['Целевая реабилитационная группа'][0]
    try:
        pod_srg = base.loc[base['СНИЛС'] == SNILS, 'дополнительная ЦРГ подгруппа №'].values[0]
        df.loc[75, 'Значение'] = pod_srg
        df.loc[76, 'Значение'] = SRG.loc[SRG['N п/п.1'] == pod_srg, 'Целевая реабилитационная подгруппа'].values[0]
    except:
        df.loc[75, 'Значение'] = ''
        df.loc[76, 'Значение'] = ''

    try:
        if df.loc[52, 'Значение'].split(', ').sort() == df.loc[53, 'Значение'].split(', ').sort(): df.loc[
            53, 'Значение'] = ''
    except:
        None

    df.loc[100:102, 'Значение'] = df.loc[62, 'Значение']
    if df.loc[71, 'Значение'] != '':
        df.loc[103, 'Значение'] = 'X'
        df.loc[104, 'Значение'] = df.loc[62, 'Значение']
        df.loc[105, 'Значение'] = 'Министерство социальной политики Свердловской области'
    else:
        df['Значение'][106] = 'X'

    # Поиск рекомендуемого адреса для прохождения пилота
    try:
        adres_town = pd.read_excel(f'{os.getcwd()}/адреса городов.xlsx')
        adres_town = adres_town.loc[adres_town['ЦРГ'] == int(df.loc[73, 'Значение'])]
        if int(df.loc[4, 'Значение'].split()[0]) < 14:
            adres_town = adres_town.loc[adres_town['Возраст'] == 'до 14']
        else:
            adres_town = adres_town.loc[adres_town['Возраст'] == '14-17']

        adres = df['Значение'][12].replace(",", "").split(' ')
        adres = adres[1:adres.index('д.') - 2]
        r = [word for word in adres if word[0].isupper()]
        for i in adres:
            try:
                r.append(int(i))
            except:
                None
        result = []
        for a in r:
            try:
                result += adres_town.loc[adres_town[
                                             'Муниципальные образования (управленческие округа)'] == a, 'Наименование учреждения'].to_list()
            except:
                None
        result = list(set([i.replace('\xa0', ' ') for i in result]))
        if len(result) == 0:
            a = 'Свердловская область (остальные МО)'
            try:
                result += adres_town.loc[adres_town[
                                             'Муниципальные образования (управленческие округа)'] == a, 'Наименование учреждения'].to_list()
            except:
                None
        result = list(set([i.replace('\xa0', ' ') for i in result]))
        df.loc[99, 'Значение'] = '\n'.join(result)
    except:
        df.loc[99, 'Значение'] = ''
        print(f'{SNILS}: Adres Error')

    # Определение предпочительного способа связи
    value = df.loc[52, 'Значение']
    number = ''
    for i in value.split():
        try:
            int(i)
            number += i
        except:
            None
    if len(number) == 11:
        v = 'X'
    elif number == '':
        try:
            int(value.replace('-', ''))
            v = 'X'
        except:
            v = ''
    else:
        try:
            int(number)
            v = 'X'
        except:
            v = ''
    df.loc[107, 'Значение'] = v

    df = df.fillna('')

    return df

def get_imge(df, doc):
    df_ = df.copy()
    img_true = InlineImage(doc, f'{os.getcwd()}/box_true.png')
    img_false = InlineImage(doc, f'{os.getcwd()}/box_false.png')
    df_.loc[df_[df_['Значение'] == 'Первая'].loc[df_['№№(МСЭ)'] == 1].index.tolist(), 'Значение'] = img_true
    df_.loc[df_[df_['Значение'] == 'Вторая'].loc[df_['№№(МСЭ)'] == 2].index.tolist(), 'Значение'] = img_true
    df_.loc[df_[df_['Значение'] == 'Третья'].loc[df_['№№(МСЭ)'] == 3].index.tolist(), 'Значение'] = img_true
    df_.loc[df_['Значение'].isin(['Первая', 'Вторая', 'Третья', 'Не установлено']) == True, 'Значение'] = img_false
    return df_


snils_list = base['СНИЛС'].to_list()[:10]
len_ = len(snils_list)
time_one = 3.04

time_all = len_ * time_one

if time_all > 60:
    time_all /= 60
    print(f'\nОбработка займет примерно {time_all} минут.\n')
else:
    print(f'\nОбработка займет примерно {time_all} секунд.\n')

for j in snils_list:
    try:
        df_1 = get_df(j)
        try:
            for i in ['МСЭ', 'родители', 'учреждение', 'ФСС']:
                doc = DocxTemplate(f'{pas}/Бланк Формы сведений о ребенке ({i}).docx')
                df = get_imge(df_1, doc)
                context = {df[f'код({i})'][j]: df['Значение'][j] for j in df.index}
                doc.render(context)

                name = f"{context['p_1_1']}.{list(context['p_1_2'])[0]}.{list(context['p_1_3'])[0]}.{i}"
                if not os.path.isdir(f"{to_pas}\\Бюро {context['p_0_2']}"):
                    os.mkdir(f"{to_pas}\\Бюро {context['p_0_2']}")
                doc.save(f"{to_pas}/Бюро {context['p_0_2']}/{name}.docx")
                number = f"{context['p_0_1']}.{context['p_0_2']}.66/2022"
                base.loc[base.loc[base['СНИЛС'] == j].index[0],
                         'Форма № (порядковый, номер бюро, код Сверд. обл./год)'] = number
            print(f'{j}: OK')
        except:
            print(f'{j}: Unknown Error')
    except:
        print(f'{j}: Not Found')

base.to_excel(f'{pas}/base.xlsx')
