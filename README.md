# Union Elections
A data gathering, cleaning, and analysis project to discover the rate of churn among USA labor union leadership. 

Our main datasource is going to be the US Department of Labor and their wonderful [website.](https://olmsapps.dol.gov/olpdr/) 

The "Yearly Data Download pulls zip archives filled with pipe delimited text documents. These will be the best way to pull the data. I will worry about automating this process for updates down the line. For now I am going to just pull the data manually.

Looks like the electronic records only go back to 2000. Could be better, but it should be enough to see whether recent events have made any noticeable impact on union electoral behavior. 

I have fairly fast internet, but nothing crazy, 200mbs up and down. The downloads were done in under 5 minutes, and that's with me needing to click 44 times. Now I gotta unzip them all. 

And just like that (this new M1 really is a beast) I have a gig of text in my repo. Not what you want, but it's a start.

Based on this sample [form](https://olmsapps.dol.gov/query/orgReport.do?rptId=739980&rptForm=LM2Form) and these less than ideal [directions](https://olmsapps.dol.gov/olpdr/Guide_to_Working_with_OLMS_LM_Data.pdf) I have identified the "ar_disbursements_emp_off_data_YYYY.txt" file as the officers disclosure, which is what we're interested in. Let's take a look at 2020, the most recent full year of data.

