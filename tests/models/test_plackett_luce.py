from openskill import Rating, rate

r = Rating()
team_1 = [r]
team_2 = [r, r]
team_3 = [r, r, r]


def test_plackett_luce():
    assert rate([team_1]) == [team_1]

    # 2P FFA
    assert rate([team_1, team_1]) == [
        [[27.63523138347365, 8.065506316323548]],
        [[22.36476861652635, 8.065506316323548]],
    ]

    # 3P FFA
    assert rate([team_1, team_1, team_1]) == [
        [[27.868876552746237, 8.204837030780652]],
        [[25.717219138186557, 8.057829747583874]],
        [[21.413904309067206, 8.057829747583874]],
    ]

    # 4P FFA
    assert rate([team_1, team_1, team_1, team_1]) == [
        [[27.795084971874736, 8.263160757613477]],
        [[26.552824984374855, 8.179213704945203]],
        [[24.68943500312503, 8.083731307186588]],
        [[20.96265504062538, 8.083731307186588]],
    ]

    # 5P FFA
    assert rate([team_1, team_1, team_1, team_1, team_1]) == [
        [[27.666666666666668, 8.290556877154474]],
        [[26.833333333333332, 8.240145629781066]],
        [[25.72222222222222, 8.179996679645559]],
        [[24.055555555555557, 8.111796013701358]],
        [[20.72222222222222, 8.111796013701358]],
    ]

    # 3 Different Sized Teams
    assert rate([team_3, team_1, team_2]) == [
        [
            [25.939870821784513, 8.247641552260456],
            [25.939870821784513, 8.247641552260456],
            [25.939870821784513, 8.247641552260456],
        ],
        [[27.21366020491262, 8.274321317985242]],
        [
            [21.84646897330287, 8.213058173195341],
            [21.84646897330287, 8.213058173195341],
        ],
    ]