import pytest

from tests.app_helper import HelpButtons


@pytest.mark.parametrize(
    argnames="text_label",
    argvalues=["*", "*" * 10, "*" * 32],
    ids=["1_symbol", "10_symbol", "32_symbol"],
)
def test_label_with_good_data_text(
    button: HelpButtons,
    text_label: str,
) -> None:
    """Test with good text, data create"""

    old_total = button.get_total_data()
    button.add_data_text(text=text_label)
    button.push_add_data_button()
    new_total = button.get_total_data()
    assert new_total == old_total + 1


@pytest.mark.parametrize(
    argnames="text_label",
    argvalues=["*" * 33, "*" * 50, "*" * 60],
    ids=["33_symbol", "50_symbol", "60_symbol"],
)
def test_text_label_max_length(
    button: HelpButtons,
    text_label: str,
) -> None:
    """check max-length text add data label"""

    button.add_data_text(text=text_label)
    assert button.get_data_text() == 32


@pytest.mark.parametrize(
    argnames="text_label",
    argvalues=["", " " * 10, " " * 32],
    ids=["none_type", "small_space", "full_space"],
)
def test_label_with_bad_data_text(
    button: HelpButtons,
    text_label: str,
) -> None:
    """Test with bad text, data don't create"""

    old_total = button.get_total_data()
    button.add_data_text(text=text_label)
    button.push_add_data_button()
    new_total = button.get_total_data()
    assert old_total == new_total


@pytest.mark.parametrize(
    argnames="count_switch_page",
    argvalues=[1, 2, 3],
    ids=["1_switch", "2_switch", "3_switch"],
)
def test_get_data_allways_go_first_page(
    button: HelpButtons,
    count_switch_page: int,
) -> None:
    """Test button GetData always switch to page 1"""

    button.push_get_data_button()
    for i in range(count_switch_page):
        button.push_next_page_button()

    button.push_get_data_button()
    assert button.get_current_page() == 1


@pytest.mark.parametrize(
    argnames="count_switch_page",
    argvalues=[1, 2, 3],
    ids=["1_switch", "2_switch", "3_switch"],
)
def test_pagination_next_with_change_page_count(
    button: HelpButtons,
    count_switch_page: int,
) -> None:
    """Test pagination next page with switch page_count and back to page 1"""

    button.push_get_data_button()
    for i in range(count_switch_page):
        button.push_next_page_button()

    button.set_items_in_list(count=count_switch_page)
    button.push_next_page_button()
    assert button.get_current_page() == 1


@pytest.mark.parametrize(
    argnames="count_switch_page",
    argvalues=[1, 2, 3],
    ids=["1_switch", "2_switch", "3_switch"],
)
def test_pagination_prev_with_change_page_count(
    button: HelpButtons,
    count_switch_page: int,
) -> None:
    """Test pagination prev page with switch page_count and back to page 1"""

    button.push_get_data_button()
    for i in range(count_switch_page):
        button.push_next_page_button()

    button.set_items_in_list(count=count_switch_page)
    button.push_prev_page_button()
    assert button.get_current_page() == 1


@pytest.mark.parametrize(
    argnames="count_switch_page",
    argvalues=[1, 2, 3],
    ids=["1_switch", "2_switch", "3_switch"],
)
def test_no_click_prev_page_when_start_page(
    button: HelpButtons,
    count_switch_page: int,
) -> None:
    """The test checks that you cannot click back on the first page"""

    button.push_get_data_button()
    assert button.get_current_page() == 1
    for i in range(count_switch_page):
        button.push_prev_page_button()

    assert button.get_current_page() == 1
