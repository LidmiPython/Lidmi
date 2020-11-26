class Load_dates:
	def __init__(self, years, month, days, hours, minutes):
		self.y = years
		self.y_t = ("год", "года", "годов")
		self.mo = month
		self.mo_t = ("месяц", "месяца", "месяцев")
		self.d = days
		self.d_t = ("день", "дня", "дней")
		self.h = hours
		self.h_t = ("час", "часа", "часов")
		self.m = minutes
		self.m_t = ("минуту", "минуты", "минут")

	def b_minutes(self):
		m = self.m
		if m == 1:
			m_res = self.m_t[0]
		elif m == 0:
			m_res = ""
		elif m == 2 or m == 3 or m == 4 or m == 22 or m == 52:
			m_res = self.m_t[1]
		elif m == 23 or m == 24 or m == 42 or m == 43 or m == 44:
			m_res = self.m_t[1]
		else:
			m_res = self.m_t[2]
		return m_res

	def b_hours(self):
		h = self.h
		if self.h == 1 or self.h == 21:
			h_res = self.h_t[0]
		elif h == 2 or h == 3 or h == 4 or h == 22 or h == 23 or h == 24:
			h_res = self.h_t[1]
		else:
			h_res = self.h_t[2]
		return h_res

	def b_days(self):
		d = self.d
		if d == 1 or d == 21 or d == 31:
			d_res = self.d_t[0]
		elif d == 2 or d == 3 or d == 4 or d == 22 or d == 23 or d == 24:
			d_res = self.d_t[1]
		else:
			d_res = self.d_t[2]
		return d_res

	def b_month(self):
		mo = self.mo
		if mo == 1:
			mo_res = self.mo_t[0]
		elif mo == 2 or mo == 3 or mo == 4:
			mo_res = self.mo_t[1]
		else:
			mo_res = self.mo_t[2]
		return mo_res

	def b_years(self):
		y = self.y
		if y == 1:
			y_res = self.y_t[0]
		elif y == 2 or y == 3 or y == 4:
			y_res = self.y_t[1]
		else:
			y_res = self.y_t[2]
		return y_res
		
def for_if_dat(years, month, days, hours, minutes):
	dat = Load_dates(years, month, days, hours, minutes)
	m = str(f"{minutes} {dat.b_minutes()}")
	h = str(f"{hours} {dat.b_hours()}")
	d = str(f"{days} {dat.b_days()}")
	mo = str(f"{month} {dat.b_month()}")
	y = str(f"{years} {dat.b_years()}")
	if years == 0 and month == 0 and days == 0 and hours == 0:
		bot_runned = str(f"{m}")
	
	elif years == 0 and month == 0 and days == 0 and hours > 0:
		if minutes == 0:
			bot_runned = str(f"{h}")
		else:
			bot_runned = str(f"{h} и {m}")

	elif years == 0 and month == 0 and days > 0:
		if hours == 0:
			if minutes == 0:
				bot_runned = str(f"{d}")
			else:
				bot_runned = str(f"{d} и {m}")
		else:
			if minutes == 0:
				bot_runned = str(f"{d} {h}")
			else:
				bot_runned = str(f"{d} {h} и {m}")
				
	elif years == 0 and month > 0:
		if days == 0:
			if hours == 0:
				if minutes == 0:
					bot_runned = str(f"{mo}")
				else:
					bot_runned = str(f"{mo} и {m}")
			else:
				if minutes == 0:
					bot_runned = str(f"{mo} и {h}")
				else:
					bot_runned = str(f"{mo} {h} и {m}")
		else:
			if hours == 0:
				if minutes == 0:
					bot_runned = str(f"{mo} {d}")
				else:
					bot_runned = str(f"{mo} {d} и {m}")
			else:
				if minutes == 0:
					bot_runned = str(f"{mo} {d} {h}")
				else:
					bot_runned = str(f"{mo} {d} {h} и {m}")

	
	elif years > 0 and month == 0:
		bot_runned = str(f"{y}")
	elif years > 0:
		bot_runned = str(f"{y} и {mo}")

	return bot_runned