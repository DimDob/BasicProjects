import unittest

from project.team import Team


class TestTeam(unittest.TestCase):
    def setUp(self) -> None:
        self.team = Team('Chelsea')

    def test_init(self):
        team = Team('chelsea')
        self.assertEqual(team.name, 'chelsea')
        self.assertEqual(team.members, {})


    def test_name_prop(self):
        with self.assertRaises(ValueError) as ex:
            team = Team('123i542!@#!@$#@%#%')
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))


    def test_add_member(self):
        self.team.members['Ivan'] = 12

        result = self.team.add_member(Petkan = 12, Ivaylo = 12 )
        self.assertEqual('Petkan' in self.team.members, True)
        self.assertEqual(self.team.members['Petkan'], 12 )
        self.assertEqual(result, "Successfully added: Petkan, Ivaylo")

    def test_remove_member_if_member_does_not_exist(self):
        self.team.members = {'Ivan':12}
        result = self.team.remove_member('Petkan')
        self.assertEqual(True, 'Petkan' not in self.team.members)
        expected = "Member with name Petkan does not exist"
        self.assertEqual(result, expected)

    def test_remove_member_if_member_exsists(self):
        self.team.members = {'Ivan':12}
        result = self.team.remove_member('Ivan')
        self.assertEqual(True, 'Ivan' not in self.team.members)
        self.assertEqual(result, 'Member Ivan removed')

    def test_gt(self):
        another_team = Team('ChernoMore')
        self.team.members = {'Ivan':12}
        self.assertEqual(True, self.team > another_team)
        self.assertEqual(False, another_team > self.team)

    def test_len(self):
        self.team.members = {'Ivan':12}
        expected = 1
        result = len(self.team)
        self.assertEqual(expected, result )

    def test_add(self):
        self.team.members = {'Ivan':12, 'Petkan':13}
        another_team = Team('Liverpool')
        another_team.members = {'Asen':15, 'Kaloyan':12}

        new_team = self.team + another_team
        self.assertEqual(new_team.name, 'ChelseaLiverpool')
        self.assertEqual({'Ivan':12, 'Petkan':13, 'Asen':15, 'Kaloyan':12}, new_team.members)

    def test_str(self):
        self.team.members = {'Ivan':12, 'Petkan':13}
        expected = f"Team name: Chelsea\n" \
                   f"Member: Petkan - 13-years old\n" \
                   f"Member: Ivan - 12-years old"
        result = str(self.team)
        self.assertEqual(expected, result )
