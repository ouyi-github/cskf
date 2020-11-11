from time import sleep

import pytest
import yaml

from web.page_workwx_main.page.page_main import Main
from web.page_workwx_main.page.page_member import AddMember


class TestAddMember:
    def setup(self):
        self.main = Main()

    @pytest.mark.skip
    @pytest.mark.parametrize("username,id,phone",yaml.safe_load(open('../data/addmember.yaml')))
    def test_add_member1(self,username,id,phone):
        addmember = self.main.goto_add_member()
        addmember.addmember_true(username,id,phone)
        assert username in addmember.getmember()

    # @pytest.mark.skip
    @pytest.mark.parametrize("username,id,phone",[('ajiufhi','nuig','15520426264')])
    def test_add_member2(self,username,id,phone):
        addmember = self.main.goto_address_list().goto_add_member()
        addmember.addmember_true(username,id,phone)
        assert addmember.getmember('zhstqdzjrq')


if __name__ == "__main__":
    pytest.main(['-v','test_main_addmember.py'])

