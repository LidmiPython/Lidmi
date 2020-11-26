import sqlite3
import time
import datetime as dt

from time_setup import date_mods as dat
from time_setup import eliefe as el
from dateutil.relativedelta import relativedelta

class DATES_SETUP:
	def __init__(self):

		self.conn = sqlite3.connect("basa_data/time.db")
		self.cursor = self.conn.cursor()
		self.timebd = time.strftime("%d.%m|%H:%M:%S")
		self.cldb = Utils()

	def CREATE_TABLE_bd_date(self):
		self.cursor.executescript('''CREATE TABLE bot_date (
				bot_date NUMERIC
			);
			''')
		self.conn.commit()
		self.cursor.execute("INSERT INTO `bot_date` (`bot_date`) VALUES(?)", (dat.r_dat,))

	def reset_date(self):
		with self.conn: 
			return self.cursor.execute("UPDATE bot_date SET bot_date = ?", (dat.r_dat,))

	def bot_runned(self):
		with self.conn:
			data1 = self.cursor.execute("SELECT * FROM `bot_date`").fetchall()
			bot_runned = self.cldb.clear_db_res(data1)
			r_year = self.cldb.r_year(bot_runned)
			r_month = self.cldb.r_month(bot_runned)
			r_days = self.cldb.r_days(bot_runned)
			r_hours = self.cldb.r_hours(bot_runned)
			r_minutes = self.cldb.r_minutes(bot_runned)
			if_else = Utils(r_year, r_month, r_days, r_hours, r_minutes)
			
			if_years = if_else.if_years()
			if_month = if_else.if_month()
			if_days = if_else.if_days()
			if_hours = if_else.if_hours()
			if_minutes = if_else.if_minutes()

			bot_runned = el.for_if_dat(if_years, if_month, if_days, if_hours, if_minutes)


			return bot_runned

class Utils:
	def __init__(self, year = None, month = None, days = None, hours = None, minutes = None):
		"""Принимает данные год, месяц, день, час, минуты (Время запуска бота)"""
		self.year = year
		self.month = month
		self.days = days
		self.hours = hours
		self.minutes = minutes

	def clear_db_res(self, db_res):
		new_data = []
		for element in db_res:
			new_data.append(element[0])
		return new_data[0]

	def r_year(self, a):
		return str(a[0]+a[1]+a[2]+a[3])

	def if_years(self):
		end = dt.datetime(int(self.year), int(self.month), int(self.days), int(self.hours), int(self.minutes))
		n = dt.datetime.now()
		relativedelta(n, end)
		relativedelta(years=+12, months=+6, days=+21, hours=+16, minutes=+25, seconds=+50, microseconds=+812805)
		return int(relativedelta(n, end).years)

	def r_month(self, a):
		if int(str(a[5]+a[6])) <= 9:
			return str(a[6])
		else:
			return str(a[5]+a[6])

	def if_month(self):
		end = dt.datetime(int(self.year), int(self.month), int(self.days), int(self.hours), int(self.minutes))
		n = dt.datetime.now()
		relativedelta(n, end)
		relativedelta(years=+12, months=+6, days=+21, hours=+16, minutes=+25, seconds=+50, microseconds=+812805)	
		return int(relativedelta(n, end).months)

	def r_days(self, a):
		if int(str(a[8]+a[9])) <= 9:
			return str(a[9])
		else:
			return str(a[8]+a[9])

	def if_days(self):
		end = dt.datetime(int(self.year), int(self.month), int(self.days), int(self.hours), int(self.minutes))
		n = dt.datetime.now()
		relativedelta(n, end)
		relativedelta(years=+12, months=+6, days=+21, hours=+16, minutes=+25, seconds=+50, microseconds=+812805)
		return int(relativedelta(n, end).days)

	def r_hours(self, a):
		if int(str(a[11]+a[12])) <= 9:
			return str(a[12])
		else:
			return str(a[11]+a[12])

	def if_hours(self):
		end = dt.datetime(int(self.year), int(self.month), int(self.days), int(self.hours), int(self.minutes))
		n = dt.datetime.now()
		relativedelta(n, end)
		relativedelta(years=+12, months=+6, days=+21, hours=+16, minutes=+25, seconds=+50, microseconds=+812805)
		return int(relativedelta(n, end).hours)

	def r_minutes(self, a):
		if int(str(a[14]+a[15])) <= 9:
			return str(a[15])
		else:
			return str(a[14]+a[15])

	def if_minutes(self):
		end = dt.datetime(int(self.year), int(self.month), int(self.days), int(self.hours), int(self.minutes))
		n = dt.datetime.now()
		relativedelta(n, end)
		relativedelta(years=+12, months=+6, days=+21, hours=+16, minutes=+25, seconds=+50, microseconds=+812805)
		return int(relativedelta(n, end).minutes)