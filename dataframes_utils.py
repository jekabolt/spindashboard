import router


def get_current_df(year, month):
    df = get_df()
    df = df[(df['get_year'] == year) & (df['get_month'] == month)]
    return df


def get_df():
    return router.goods_df.copy()


def get_current_goods_acceptance(year, month):
    return get_current_goods_acceptance_df(year, month)['Storage']


def get_current_goods_acceptance_active(year, month):
    goods_df = get_current_goods_acceptance_df(year, month)
    goods_acceptance = goods_df.copy()
    goods_acceptance = goods_acceptance[goods_acceptance['Status'] == 'Приемка']
    return goods_acceptance['Storage']


def get_all_time_goods_acceptance_active():
    goods_df = get_all_time_goods_acceptance_df()
    goods_acceptance = goods_df.copy()
    goods_acceptance = goods_acceptance[goods_acceptance['Status'] == 'Приемка']
    return goods_acceptance['Storage']


def get_current_goods_acceptance_df(year, month):
    df = get_current_df(year, month)
    df['Storage'] = df.Storage.fillna('Не указано')
    return df


def get_all_time_goods_acceptance_df():
    df = get_df()
    df['Storage'] = df.Storage.fillna('Не указано')
    return df


def count_map(df):
    goods_map = {}
    total_count = 0
    for key in df:
        if key in goods_map:
            goods_map[key] += 1
            total_count += 1
        else:
            goods_map[key] = 1
            total_count += 1
    return goods_map, total_count
