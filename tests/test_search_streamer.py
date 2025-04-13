def test_search_and_visit_starcraft_streamer(home_page, search_results_page, streamer_page):
    """
    Test case to search for StarCraft II streamers on Twitch and visit one.
    """
    home_page.navigate_to_twitch_tv()
    home_page.accept_cookies_if_present()
    home_page.search_for("StarCraft II")
    search_results_page.scroll_down_times(2)
    search_results_page.select_streamer()
    streamer_page.take_screenshot("starcraft_streamer")
