Feature: Register User
  As a developer this is my first bdd project
  Scenario: open register website
    When I open the register website "http://www.5itest.cn/register"
    Then I except that the title is "注册"
  Scenario: input username
    When I set with useremail "1111@163.com"
    And I set with username "11001s"
    And I set with password "110111"
    And I set with code "12345"
    And I click with registerbutton
    Then I except that text "验证码错误"