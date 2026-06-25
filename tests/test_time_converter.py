import pytest

from d8s_converters import (
    centuries_to_days,
    centuries_to_fortnights,
    centuries_to_hours,
    centuries_to_millenniums,
    centuries_to_minutes,
    centuries_to_months,
    centuries_to_seconds,
    centuries_to_weeks,
    centuries_to_years,
    days_to_centuries,
    days_to_fortnights,
    days_to_hours,
    days_to_millenniums,
    days_to_minutes,
    days_to_months,
    days_to_seconds,
    days_to_weeks,
    days_to_years,
    fortnights_to_centuries,
    fortnights_to_days,
    fortnights_to_hours,
    fortnights_to_millenniums,
    fortnights_to_minutes,
    fortnights_to_months,
    fortnights_to_seconds,
    fortnights_to_weeks,
    fortnights_to_years,
    hours_to_centuries,
    hours_to_days,
    hours_to_fortnights,
    hours_to_millenniums,
    hours_to_minutes,
    hours_to_months,
    hours_to_seconds,
    hours_to_weeks,
    hours_to_years,
    millenniums_to_centuries,
    millenniums_to_days,
    millenniums_to_fortnights,
    millenniums_to_hours,
    millenniums_to_minutes,
    millenniums_to_months,
    millenniums_to_seconds,
    millenniums_to_weeks,
    millenniums_to_years,
    minutes_to_centuries,
    minutes_to_days,
    minutes_to_fortnights,
    minutes_to_hours,
    minutes_to_millenniums,
    minutes_to_months,
    minutes_to_seconds,
    minutes_to_weeks,
    minutes_to_years,
    months_to_centuries,
    months_to_days,
    months_to_fortnights,
    months_to_hours,
    months_to_millenniums,
    months_to_minutes,
    months_to_seconds,
    months_to_weeks,
    months_to_years,
    seconds_to_centuries,
    seconds_to_days,
    seconds_to_fortnights,
    seconds_to_hours,
    seconds_to_millenniums,
    seconds_to_minutes,
    seconds_to_months,
    seconds_to_weeks,
    seconds_to_years,
    weeks_to_centuries,
    weeks_to_days,
    weeks_to_fortnights,
    weeks_to_hours,
    weeks_to_millenniums,
    weeks_to_minutes,
    weeks_to_months,
    weeks_to_seconds,
    weeks_to_years,
    years_to_centuries,
    years_to_days,
    years_to_fortnights,
    years_to_hours,
    years_to_millenniums,
    years_to_minutes,
    years_to_months,
    years_to_seconds,
    years_to_weeks,
)


def test_centuries_to_days_docs_1():
    assert centuries_to_days(1) == pytest.approx(36525.0)


def test_centuries_to_fortnights_docs_1():
    assert centuries_to_fortnights(1) == pytest.approx(2608.928571428571)


def test_centuries_to_hours_docs_1():
    assert centuries_to_hours(1) == pytest.approx(876600.0)


def test_centuries_to_millenniums_docs_1():
    assert centuries_to_millenniums(1) == pytest.approx(0.1)


def test_centuries_to_minutes_docs_1():
    assert centuries_to_minutes(1) == pytest.approx(52596000.0)


def test_centuries_to_months_docs_1():
    assert centuries_to_months(1) == pytest.approx(1200.0)


def test_centuries_to_seconds_docs_1():
    assert centuries_to_seconds(1) == pytest.approx(3155760000.0)


def test_centuries_to_weeks_docs_1():
    assert centuries_to_weeks(1) == pytest.approx(5217.857142857142)


def test_centuries_to_years_docs_1():
    assert centuries_to_years(1) == pytest.approx(100.0)


def test_days_to_centuries_docs_1():
    assert days_to_centuries(1) == pytest.approx(2.7378507871321012e-05)


def test_days_to_fortnights_docs_1():
    assert days_to_fortnights(1) == pytest.approx(0.07142857142857142)


def test_days_to_hours_docs_1():
    assert days_to_hours(1) == pytest.approx(24.0)


def test_days_to_millenniums_docs_1():
    assert days_to_millenniums(1) == pytest.approx(2.737850787132101e-06)


def test_days_to_minutes_docs_1():
    assert days_to_minutes(1) == pytest.approx(1440.0)


def test_days_to_months_docs_1():
    assert days_to_months(1) == pytest.approx(0.03285420944558522)


def test_days_to_seconds_docs_1():
    assert days_to_seconds(1) == pytest.approx(86400)


def test_days_to_weeks_docs_1():
    assert days_to_weeks(1) == pytest.approx(0.14285714285714285)


def test_days_to_years_docs_1():
    assert days_to_years(1) == pytest.approx(0.0027378507871321013)


def test_fortnights_to_centuries_docs_1():
    assert fortnights_to_centuries(1) == pytest.approx(0.0003832991101984942)


def test_fortnights_to_days_docs_1():
    assert fortnights_to_days(1) == pytest.approx(14.0)


def test_fortnights_to_hours_docs_1():
    assert fortnights_to_hours(1) == pytest.approx(336.0)


def test_fortnights_to_millenniums_docs_1():
    assert fortnights_to_millenniums(1) == pytest.approx(3.832991101984942e-05)


def test_fortnights_to_minutes_docs_1():
    assert fortnights_to_minutes(1) == pytest.approx(20160.0)


def test_fortnights_to_months_docs_1():
    assert fortnights_to_months(1) == pytest.approx(0.459958932238193)


def test_fortnights_to_seconds_docs_1():
    assert fortnights_to_seconds(1) == pytest.approx(1209600)


def test_fortnights_to_weeks_docs_1():
    assert fortnights_to_weeks(1) == pytest.approx(2.0)


def test_fortnights_to_years_docs_1():
    assert fortnights_to_years(1) == pytest.approx(0.038329911019849415)


def test_hours_to_centuries_docs_1():
    assert hours_to_centuries(1) == pytest.approx(1.140771161305042e-06)


def test_hours_to_days_docs_1():
    assert hours_to_days(1) == pytest.approx(0.041666666666666664)


def test_hours_to_fortnights_docs_1():
    assert hours_to_fortnights(1) == pytest.approx(0.002976190476190476)


def test_hours_to_millenniums_docs_1():
    assert hours_to_millenniums(1) == pytest.approx(1.1407711613050421e-07)


def test_hours_to_minutes_docs_1():
    assert hours_to_minutes(1) == pytest.approx(60.0)


def test_hours_to_months_docs_1():
    assert hours_to_months(1) == pytest.approx(0.0013689253935660506)


def test_hours_to_seconds_docs_1():
    assert hours_to_seconds(1) == pytest.approx(3600)


def test_hours_to_weeks_docs_1():
    assert hours_to_weeks(1) == pytest.approx(0.005952380952380952)


def test_hours_to_years_docs_1():
    assert hours_to_years(1) == pytest.approx(0.00011407711613050422)


def test_millenniums_to_centuries_docs_1():
    assert millenniums_to_centuries(1) == pytest.approx(10.0)


def test_millenniums_to_days_docs_1():
    assert millenniums_to_days(1) == pytest.approx(365250.0)


def test_millenniums_to_fortnights_docs_1():
    assert millenniums_to_fortnights(1) == pytest.approx(26089.285714285714)


def test_millenniums_to_hours_docs_1():
    assert millenniums_to_hours(1) == pytest.approx(8766000.0)


def test_millenniums_to_minutes_docs_1():
    assert millenniums_to_minutes(1) == pytest.approx(525960000.0)


def test_millenniums_to_months_docs_1():
    assert millenniums_to_months(1) == pytest.approx(12000.0)


def test_millenniums_to_seconds_docs_1():
    assert millenniums_to_seconds(1) == pytest.approx(31557600000.0)


def test_millenniums_to_weeks_docs_1():
    assert millenniums_to_weeks(1) == pytest.approx(52178.57142857143)


def test_millenniums_to_years_docs_1():
    assert millenniums_to_years(1) == pytest.approx(1000.0)


def test_minutes_to_centuries_docs_1():
    assert minutes_to_centuries(1) == pytest.approx(1.9012852688417368e-08)


def test_minutes_to_days_docs_1():
    assert minutes_to_days(1) == pytest.approx(0.0006944444444444444)


def test_minutes_to_fortnights_docs_1():
    assert minutes_to_fortnights(1) == pytest.approx(4.9603174603174596e-05)


def test_minutes_to_hours_docs_1():
    assert minutes_to_hours(1) == pytest.approx(0.016666666666666666)


def test_minutes_to_millenniums_docs_1():
    assert minutes_to_millenniums(1) == pytest.approx(1.901285268841737e-09)


def test_minutes_to_months_docs_1():
    assert minutes_to_months(1) == pytest.approx(2.2815423226100844e-05)


def test_minutes_to_seconds_docs_1():
    assert minutes_to_seconds(1) == pytest.approx(60)


def test_minutes_to_weeks_docs_1():
    assert minutes_to_weeks(1) == pytest.approx(9.920634920634919e-05)


def test_minutes_to_years_docs_1():
    assert minutes_to_years(1) == pytest.approx(1.901285268841737e-06)


def test_months_to_centuries_docs_1():
    assert months_to_centuries(1) == pytest.approx(0.0008333333333333333)


def test_months_to_days_docs_1():
    assert months_to_days(1) == pytest.approx(30.4375)


def test_months_to_fortnights_docs_1():
    assert months_to_fortnights(1) == pytest.approx(2.174107142857143)


def test_months_to_hours_docs_1():
    assert months_to_hours(1) == pytest.approx(730.5)


def test_months_to_millenniums_docs_1():
    assert months_to_millenniums(1) == pytest.approx(8.333333333333333e-05)


def test_months_to_minutes_docs_1():
    assert months_to_minutes(1) == pytest.approx(43830.0)


def test_months_to_seconds_docs_1():
    assert months_to_seconds(1) == pytest.approx(2629800.0)


def test_months_to_weeks_docs_1():
    assert months_to_weeks(1) == pytest.approx(4.348214285714286)


def test_months_to_years_docs_1():
    assert months_to_years(1) == pytest.approx(0.08333333333333333)


def test_seconds_to_centuries_docs_1():
    assert seconds_to_centuries(60) == pytest.approx(1.9012852688417368e-08)


def test_seconds_to_days_docs_1():
    assert seconds_to_days(60) == pytest.approx(0.0006944444444444444)


def test_seconds_to_fortnights_docs_1():
    assert seconds_to_fortnights(60) == pytest.approx(4.9603174603174596e-05)


def test_seconds_to_hours_docs_1():
    assert seconds_to_hours(60) == pytest.approx(0.016666666666666666)


def test_seconds_to_millenniums_docs_1():
    assert seconds_to_millenniums(60) == pytest.approx(1.901285268841737e-09)


def test_seconds_to_minutes_docs_1():
    assert seconds_to_minutes(60) == pytest.approx(1.0)


def test_seconds_to_months_docs_1():
    assert seconds_to_months(60) == pytest.approx(2.2815423226100844e-05)


def test_seconds_to_weeks_docs_1():
    assert seconds_to_weeks(60) == pytest.approx(9.920634920634919e-05)


def test_seconds_to_years_docs_1():
    assert seconds_to_years(60) == pytest.approx(1.901285268841737e-06)


def test_weeks_to_centuries_docs_1():
    assert weeks_to_centuries(1) == pytest.approx(0.0001916495550992471)


def test_weeks_to_days_docs_1():
    assert weeks_to_days(1) == pytest.approx(7.0)


def test_weeks_to_fortnights_docs_1():
    assert weeks_to_fortnights(1) == pytest.approx(0.5)


def test_weeks_to_hours_docs_1():
    assert weeks_to_hours(1) == pytest.approx(168.0)


def test_weeks_to_millenniums_docs_1():
    assert weeks_to_millenniums(1) == pytest.approx(1.916495550992471e-05)


def test_weeks_to_minutes_docs_1():
    assert weeks_to_minutes(1) == pytest.approx(10080.0)


def test_weeks_to_months_docs_1():
    assert weeks_to_months(1) == pytest.approx(0.2299794661190965)


def test_weeks_to_seconds_docs_1():
    assert weeks_to_seconds(1) == pytest.approx(604800)


def test_weeks_to_years_docs_1():
    assert weeks_to_years(1) == pytest.approx(0.019164955509924708)


def test_years_to_centuries_docs_1():
    assert years_to_centuries(1) == pytest.approx(0.01)


def test_years_to_days_docs_1():
    assert years_to_days(1) == pytest.approx(365.25)


def test_years_to_fortnights_docs_1():
    assert years_to_fortnights(1) == pytest.approx(26.08928571428571)


def test_years_to_hours_docs_1():
    assert years_to_hours(1) == pytest.approx(8766.0)


def test_years_to_millenniums_docs_1():
    assert years_to_millenniums(1) == pytest.approx(0.001)


def test_years_to_minutes_docs_1():
    assert years_to_minutes(1) == pytest.approx(525960.0)


def test_years_to_months_docs_1():
    assert years_to_months(1) == pytest.approx(12.0)


def test_years_to_seconds_docs_1():
    assert years_to_seconds(1) == pytest.approx(31557600.0)


def test_years_to_weeks_docs_1():
    assert years_to_weeks(1) == pytest.approx(52.17857142857142)
