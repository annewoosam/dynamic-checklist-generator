-- NOTE that sqlalchemy/database.sql is a symbolic link to sql/database.sql. ALL changes will be reflected in the sqlalchemy assessment.

CREATE TABLE users (
    user_id VARCHAR(5) PRIMARY KEY,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50),
    user_name VARCHAR(50),
    user_type VARCHAR(50)
);

CREATE TABLE templates (
    template_id SERIAL PRIMARY KEY,
    template_name VARCHAR(50) NOT NULL,
    user_id VARCHAR(5),
    updated_at DATE
);

-- Create an Awards Table

CREATE TABLE template_questions (
                     template_name VARCHAR NOT NULL,
                     template_question_id SERIAL PRIMARY KEY,
                     question VARCHAR NOT NULL,
                     yes_text VARCHAR NOT NULL,
                     no_text VARCHAR NOT NULL,
                     not_applicable_text VARCHAR NOT NULL,
                     help_text VARCHAR NOT NULL,
                     resource_url VARCHAR NOT NULL,
                     category VARCHAR NOT NULL,
                     primary_driver BOOLEAN NOT NULL,
                     );

CREATE TABLE checklist (
                     checklist_id SERIAL PRIMARY KEY,
                     template_name VARCHAR NOT NULL,
                     timeframe DATE NOT NULL,
                     who_for VARCHAR NOT NULL,

                     date_sent_to_review DATE,  
                     reviewer_full_name VARCHAR,
                     reviewer_email VARCHAR,
 
                     date_review_completed DATE,   
                     recipient_full_name VARCHAR,
                     recipient_email VARCHAR, 
                     date_sent_to_recipient DATE

                     preparer_answer VARCHAR,
                     preparer_time_spent INTEGER,
                     preparer_comment VARCHAR,

                     reviewer_answer VARCHAR,                     
                     reviewer_time_spent INTEGER,
                     reviewer_comment VARCHAR,
                     );

-- Insert Users
INSERT INTO users (user_id, email, password, user_name, user_type) VALUES
(1, 'annewoosamcode@gmail.com', 'testac','Anne Woo-Sam','creator'),
(2, 'retiringwiser@gmail.com', 'testrw', 'Hoot Owl','preparer'),
(3, 'strategicartscollaborative@gmail.com', 'testsa', 'Strategic Arts','reviewer');

-- Insert a Template Name
INSERT INTO templates (template_id, template_name, user_id, updated_at) VALUES
(1, 'compliance testing', 1, '2020-08-11'),
(2, 'client compliance guide', 1, '2020-08-11');

INSERT INTO template_questions (template_name, template_question_id, question, yes_text, no_text, not_applicable_text,help_text,resource_url,
                                category, primary_driver)
VALUES
('compliance testing', 1, '1. Has the census been received?', 'Census received','Census missing. Plan is/will be placed on hold.','A census must be provided. Not applicable is not an appropriate response.','If the census is missing, e-mail the relationship manager immediately prepare the folders and pull any reporting such as trust statements and start the trust reconciliation. Once you have gotten as far as possible, place the plan on hold.','https://www.youtube.com','CENSUS',false),
('compliance testing', 2, '2. Has the questionnaire been received?', 'Questionnaire received.','Questionnaire not received. Request. If the client appears to answer the same way each year move forward and ask the client to send a Questionnaire, confirm results.','not_applicable-text','help_text','https://www.youtube.com','category',false),
('compliance testing', 3, '3. Is the census formatted in a format that can be directly loaded into the system?', 'Census is in a format ready for load.','no_text','not_applicable-text','help_text','https://www.youtube.com','category',false),
('compliance testing', 4, '4. Has the census been loaded to the system?', 'Census loaded.','Census must be formatted before it can be loaded.','An invalid response for whether the census was loaded was entered.  Choose either Y or N.','help_text','https://www.youtube.com','category',false),
('compliance testing', 5, '5. Has an Eligibility proof been prepared from the census that separates employees into the categories HCEs, NHCEs, Ineligibles(with explanation such as age,service), Excluded, Prior Year Terms?', 'Eligibility Proof employee classifications have been made.','Eligibility Proof employee classifications need to be made.','An invalid response for the Eligibility Proof employee classification step was entered. Choose either Y or N.','help_text','https://www.youtube.com','category',false),
('compliance testing', 6, '6. Does the proof indicate the HCEs percentages, relationships and attribution for all employees with the same name as owner-employees, those earning over $120,000 in a prior year?', 'Owner percentages, relationships for those with the same last name as the owners and other relatives, and persons making over $120,000 in the last year have been marked in the file.','Census must be formatted before it can be loaded.','No valid response entered Enter Y, N or NA to indicate whether all owner percentages, relationships for those with the same last name as the owners and other relatives, and persons making over $120,000 in the last year have been marked in the file.','help_text','https://www.youtube.com','category',false),
('compliance testing', 7, '7. Does the proof indicate the estimated Actual Deferral Percentage and properly cap the deferrals and the compensation considered at the at the limit for the year tested?"', 'Preliminary ADP ACP Results have been calculated and compared to the reports generated by the system. Variances have been resolved.','Update the file with owner percentages, mark family with a 1 in the family/spouse/lineal descendant area or potential family relationships with a Y or N and flag persons making over 120,000 in the prior year with a Y as needed.','This plan does not have deferrals or match. ADP ACP testing does not apply','help_text','https://www.youtube.com','category',false),
('compliance testing', 8, '8. Have you indicated whether the plan uses Prior Year Testing and confirmed that the system is correctly set-up for Prior Year Testing?', 'The Prior Year Testing numbers have been entered.','Preliminary ADP ACP Results have NOT been calculated and compared to the reports generated by the system. OR Variances have been resolved.','The plan does not use prior year testing.','help_text','https://www.youtube.com','category',false),
('compliance testing', 9, '9. Have you confirmed the formula for any Match and ensured it is entered in the testing system? Enter NA if the plan either does not have a match source or will not be funding a match this year.', 'Match formula confirmed and entered and results checked.','Enter the match formula into the system after confirming it against the document/client questionnaire/prior practice. If using a prior formula, indicate in Results sent to client.','The plan does not have a match source or is not funding the match this year.','help_text','https://www.youtube.com','category',false),
('compliance testing', 10, '10. Have you confirmed the formula for any Safe Harbor Match and ensured it is entered in the testing system?', 'Safe Harbor match formula confirmed and entered and results checked.','The plan does not have a Safe Harbor match source or is not funding the match this year.',' No valid response entered. Please enter a Y,N or NA as to whether the plan uses a Safe Harbor match and you have entered the formula into the system and checked the calculation.','help_text','https://www.youtube.com','category',false),
('compliance testing', 11, '11. Have you verified the Match if the plan requires calculation and is on an annual basis according to the plan document/adoption agreement?', 'Match basis has been checked and whether a calculation is required was verified.','Match basis (annual or not) or whether a calculation is needed must be verified.','There is no Match source or the match is not being funded this year.','help_text','https://www.youtube.com','category',false),
('compliance testing', 12, '12. If the plan is a sole proprietorship or partnership and has Schedule C or Schedule K income that is not passing through as W-2 income, has the owner/all partners signed participation agreements?', 'All participation agreements for participating employers signed.','Participating agreements missing/amendment and filing required.','Participation agreements do not apply to this plan.','help_text','https://www.youtube.com','category',false),
('compliance testing', 13, '13. Has the income for sole proprietors/partners been entered correctly based on either Draft or final Schedule C or K-1 documents? Search for Entity Type in the plan document/adoption agreement to identify if the plan is a sole proprietorship/partnership not taxed as a corporation.', 'Schedule C or K income entered completely on file and draft or final schedules provided.','Provide Schedule C or K income and draft or final schedules.','The plan is not a sole proprietorship or a partnership. Therefore Schedule C or K income does not have to be provided.','help_text','https://www.youtube.com','category',false),
('compliance testing', 14, '14. Did you load and generate the ADP and ACP Tests?', 'ADP ACP tests generated.','Generate ADP ACP tests.','The plan does not have deferrals/match.','help_text','https://www.youtube.com','category',false),
('compliance testing', 15, '15. Do the ADP and ACP tests match your expectations on the proof or if not have you explained the differences and made the adjustments needed to tie out the system to the census?', 'ADP and ACP tests match expectations based on proof/prior testing review.','ADP and ACP tests do not match expectations based on proof/prior testing review.','The plan does not have deferrals/match.','help_text','https://www.youtube.com','category',false),
('compliance testing', 16, '16. Has all the income for employees been accounted for?', 'All employee income accounted for.','Employee income appears to be missing. Contact client.','Not a valid response. Enter Y or N as to whether all employee income is accounted for.','help_text','https://www.youtube.com','category',false),
('compliance testing', 17, '17. Did the client provide excluded compensation for the Match calculation?', 'Excluded Compensation was provided for the match.','Excluded Compensation needed for the match. Contact client.','There is no excluded compensation for the match or the match is not being funded or the plan does not have a match source.','help_text','https://www.youtube.com','category',false),
('compliance testing', 18, '18. Have you checked for plan Match excesses if the plan Match is on an allocation or payroll period basis?', 'Match excess checked.','Check for Match excesses.','Match excesses do not need to be checked because there is no match or the plan match is now being calculated and has not been funded yet.','help_text','https://www.youtube.com','category',false),
('compliance testing', 19, '19. Have you prepared the Match Contribution file for either the contribution/calculation or excesses?', 'The match file has been prepared.','The Match file needs to be prepared.','Not applicable. No match is being funded or the match funded is the same as that confirmed by the system.','help_text','https://www.youtube.com','category',false),
('compliance testing', 20, '20. Did the client provide the formula and classes for the Profit Sharing or Nonelective calculation? Enter N if the client was undecided. Enter NA if no Profit Sharing source or contribution to be made.', 'The Profit Sharing/Nonelective formula was provided or is specified in the document.','The Profit sharing/nonelective formula must be obtained from the plan sponsor.','The Profit Sharing/nonelective formula is not needed because the source does not apply to this plan or the source will not be funded this year.','help_text','https://www.youtube.com','category',false),
('compliance testing', 21, '21. Did the client provide excluded compensation for the Profit Sharing or Nonelective calculation?', 'Excluded compensation was provided.','Excluded compensation must be provided.','Excluded compensation is not allowed in this plan.','help_text','https://www.youtube.com','category',false),
('compliance testing', 22, '22. If the plan is cross-tested, that is, every individual is in their own class and is making a Profit Sharing/Nonelective contribution have you confirmed the formula calculations?', 'Profit Sharing/Nonelective calculations have been confirmed.','Profit Sharing/Nonelective calculations must be confirmed.','Profit Sharing/Nonelective Calculations do not apply because the source is not permitted or because no funding will be made this year.','help_text','https://www.youtube.com','category',false),
('compliance testing', 23, '23. Have you prepared the Profit Sharing/Nonelective Contribution file for either the contribution/calculation or excesses?', 'Profit Sharing/nonelective contribution file prepared.','Profit Sharing/nonelective contribution file must be prepared.','No Profit Sharing/Nonelective file is required as the source does not exist or there will be no funding this year.','help_text','https://www.youtube.com','category',false),
('compliance testing', 24, '24. Have you confirmed that HCEs by Attribution are identified in the file?', 'Owner family members and persons with same last name as owners have relationship to owners identified.','Identify owner family members and relationship to owners of people with the same last name.','No owners in the plan.','help_text','https://www.youtube.com','category',false),
('compliance testing', 25, '25. Did you load the participant source activity?', 'Participant contribution by source loaded.','Participant contribution by source must be loaded.','There is no participant contribution activity to load.','help_text','https://www.youtube.com','category',false),
('compliance testing', 26, '26. Have you printed the Top Heavy Test for next testing year and the current allocation if the plan is not a 100% Union or 403(b) plan and one of the following situations apply: The plan is receiving (1) Deferrals only, (2) Deferrals and Match only or (3) Deferrals and a Safe Harbor contribution and is making Profit Sharing/Nonelective contributions?', 'Top Heavy Allocation & Test Printed.','Print Top Heavy Allocation & Test.','Top Heavy Allocation & Test do not apply.','help_text','https://www.youtube.com','category',false),
('compliance testing', 27, '27. Did you load vesting?', 'Vesting loaded.','Load vesting.','Vesting load does not apply.','help_text','https://www.youtube.com','category',false),
('compliance testing', 28, '28. Did you confirm census contributions against the trust and provide a true-up file for any variances?', 'Trust accounting complete.','Complete trust accounting.','Trust accounting does not apply.','help_text','https://www.youtube.com','category',false),
('compliance testing', 29, '29. Has the client responded to all questions?', 'Client has responded to all questions.','Follow-up with client on questions.','Client questions do not apply.','help_text','https://www.youtube.com','category',false),
('compliance testing', 30, '30. Have all the client responses been entered?', 'Client responses all entered.','Enter client responses.','Client responses not applicable.','help_text','https://www.youtube.com','category',false),
('compliance testing', 31, '31. Have you regenerated the reports and re-confirmed the numbers?', 'Reports reprinted and re-reconciled.','Reprint reports and re-reconcile.','Reprinting reports and re-reconciling not applicable.','help_text','https://www.youtube.com','category',false),
('compliance testing', 32, '32. Did you print the Title Page?', 'Title page printed.','Print title page.','not_applicable-text','help_text','https://www.youtube.com','category',false),
('compliance testing', 33, '33. Did you print the Table of Contents?', 'Table of contents printed.','Print table of contents.','Title page is not applicable.','help_text','https://www.youtube.com','category',false),
('compliance testing', 34, '34. Did you print the Results Summary?', 'Results summary printed.','Print results summary.','Table of contents not applicable.','help_text','https://www.youtube.com','category',false),
('compliance testing', 35, '35. Did you print the ADP and ACP Nondiscrimination Test or ADP Nondiscrimination Test, as applies?', 'ADP/ACP report printed.','Print ADP/ACP report.','not_applicable-text','help_text','https://www.youtube.com','category',false),
('compliance testing', 36, '36. Did you print the Catch-Up Contributions Summary?', 'Catch-Up contribution report printed.','Print Catch-up contribution report.','Results summary not applicable.','help_text','https://www.youtube.com','category',false),
('compliance testing', 37, '37. Did you print the Annual Additions Test?', 'Annual Additions report printed.','Print Annual Additions report.','ADP/ACP report not applicable.','help_text','https://www.youtube.com','category',false),
('compliance testing', 38, '38. Did you print the General Test under 401(a)(4)?', 'General Test printed.','Print General Test.','General test does not apply.','help_text','https://www.youtube.com','category',false),
('compliance testing', 39, '39. Did you print the Budget Report for Sole Proprietorships/Partnerships with Schedule C or K income?', 'Budget printed.','Print Budget.','Budget does not apply.','help_text','https://www.youtube.com','category',false),
('compliance testing', 40, '40. Did you print the 414(s) test if excluded compensation other than 125, reimbursements or date of participation compensation was used?', '414(s) printed.','414(s) not printed.','414(s) does not apply.','help_text','https://www.youtube.com','category',false),
('compliance testing', 41, '41. Did you place a copy of the census in the working papers folder, all review files in the Review Folder and all Client Files including reports and contribution and refund files in the Client Folder?', 'Files saved to folders.','Save files to folders.','Saving files to folders does not apply.','help_text','https://www.youtube.com','category',false),
('compliance testing', 42, '42. Did you enter the contributions for deferrals and roth for the three relevant periods as necessary if the plan is an Off-Calendar (fiscal year end) plan?', 'Off-calendar 402(g) numbers entered.','Enter off-calendar 402(g) numbers.','402(g) numbers do not apply.','help_text','https://www.youtube.com','category',false),
('compliance testing', 43, '43. Did you update vesting to 100% if the plan terminated and has a signed termination agreement and did you adjust the testing compensation by the ratio of months in the plan year based on the year end date?', 'Plan Termination vesting updated.','Update vesting for plan termination.','not_applicable-text','help_text','https://www.youtube.com','category',false),
('compliance testing', 44, '44. For plans with Short Plan Years did you adjust the testing compensation, the deferral limits and any required hours for testing?"', 'Short Plan Year compensation, deferral limits and hours adjustments made.','Make adjustments to compensation limit, deferral limit and hours for short plan year.','Plan is not terminating - vesting update to 100% not applicable.','help_text','https://www.youtube.com','category',false),
('compliance testing', 45, '45. Has the relevant tracking database been updated?', 'Tracking database updated.','Update tracking database.','Tracking database update not applicable.','help_text','https://www.youtube.com','category',false),
('compliance testing', 46, '46. If the plan had late deferrals, have you logged a request to prepare a submission in the relevant tracking database?', 'Late deferrals tracking record created.','Log a late deferrals tracking record.','A late deferrals tracking record is not needed.','help_text','https://www.youtube.com','category',false),
('compliance testing', 47, '47. Have you logged a request to begin preparation of the 5500, Summary Annual Report and 8955-SSA in the relevant tracking database?', 'Government Forms Tracking created.','Add Government Forms tracking.','Government Forms tracking is not needed for this plan.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 48, 'Is your file organized with the same top row as the initial file downloaded?', 'Headers fine.','Fix headers.','We assumed headers do not apply to your file. It is a custom file. This will likely slow down processing because the file will need to be manually formatted instead fo automatically processed.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 49, 'Apply a filter across the rows in the original template. When you filter social security numbers are there any blanks?', 'Social Security Numbers fine.','Fix social security numbers.','You answered N/A. We can use employee ID numbers to load a file when social security numbers are not available. All employees must have employee IDs in order to link their information from year to year and avoid confusion when employees have similar names.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 50, 'When you filter dates of birth are there any blanks?', 'Dates of Birth Fine.','Fix Dates of Birth.','Warning! All files should have dates of birth.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 51, 'When you filter dates of birth are there any for persons under 18', 'Dates of birth for young employees are correct.','Fix dates of birth for employees that make them younger than they are.','No employees are under 18.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 52, 'When you filter dates of birth are there any for persons over 80 who should not be', 'Retiree dates of hire fine.','Fix dates of birth for retiree hires.','There are no retiree age hires.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 53, 'When you filter dates of hire are there any blanks', 'Dates of Hire fine.','Fix dates of hire.','All employees must have a valid date of hire. Correct the file and change your answer to Y.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 54, 'Are there any blank dates of rehire for persons who have a termination date prior to this year and received compensation?', 'Dates of Rehire fine.','Fix dates of rehire.','Dates of rehire did not apply.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 55, 'Are there any termination dates for people before rehire dates?', 'Dates of rehire after termination fine.','Fix dates of rehire.','There are no dates of rehire to correct.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 56, 'When you apply a filter do you have percentages in the ownership column that add up to 100% or is not have you explained on tab 2?', 'Owners identified.','Enter owner percentages onto the file.','If there are no owners, note on tab 2.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 57,'Have you placed a Y in the officer column for each officer or explained on tab 2 that there are no officers', 'Officers have been marked in the file.','Mark officers.','No officers are employees.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 58,'Have you indicated the relationship of all family members for anyone who has a relationship to the owner(s)?', 'Family attribution has been noted in the file, including for persons with the same last names as the owners.','Fix family attribution including noting relationship of persons with the same last name as the owners.','There is no ownership in this plan or persons with the same last name as the owners','help_text','https://www.youtube.com','category',false),
('client compliance guide', 59,'Have you entered a formula for the Match or entered no match on tab 2?', 'Match contributions clarified - either none or for yes, formula and principal class numbers and budget provided.','Provide match answer and formula if funding.','Match does not apply.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 60,'Have you entered a formula for Profit Sharing including the class of each person based on how much Profit Sharing they should receive if eligible in the Principal column?', 'Profit sharing/nonelective contributions clarified - either none or for yes, formula and principal class numbers and budget provided.','Provide Profit Sharing formula, and if, each class is its own separate group in the plan document(adoption agreement), add a principal code column to your spreadsheet and enter the group number to use for each eligible individual. On tab 2 identify the target percentage or dollar amount for each group or the plan as a whole.','"Profit Sharing or nonelective contributions will not be made for this testing year.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 61,'Excluded Compensation must be excluded in the plan document to be disregarded in calculating the Match/Profit Sharing. Have you confirmed that you did not enter the same amount as the compensation for participants not yet eligible to participate in the plan?', 'Excluded compensation provided.','Provide excluded compensation.','No excluded compensation is permitted in the plan document(adoption agreement) or the plan can use excluded compensation but chooses not to and is passing all tests and not funding any employer contributions such as a match or profit sharing or nonelective contribution, whether regular or Safe Harbor.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 62,'Excluded Employees must be excluded in the plan document to be disregarded in testing. Have you marked all these employees with a Y?', 'Excluded employees marked - fine.','Mark excluded employees.','There were no excluded employees.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 63,'If your plan transferred to us in the middle of the plan year, did you provide the prior testing results?', 'Prior testing results provided.','Prior testing results need to be provided.','Prior testing results do not need to be provided because the plan was tested at the current provider last year or the first testing year is this year.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 64,'If your plan transferred to us in the middle of the plan year, did you provide the prior custodian statement of contributions by participant by money type(source)?', 'Prior contribution data was provided.','Provide prior contribution information.','All activity for the testing year was conducted at the same provider. There were no conversions from another provider or outside accounts.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 65,'If your entity is a Sole Proprietorship or Partnership have you entered Schedule C or Schedule K income on the spreadsheet and provided draft or actual Schedules?', 'Schedule C or K income entered comepletely on file and draft or final schedules provided.','Provide Schedule C or K income and draft or final schedules.','The plan is not a sole proprietorship or a partnership. Therefore Schedule C or K income does not have to be provided.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 66,'Have you identified any Schedule K recipients who are actually receiving income as W-2 income?', 'Schedule K participants receiving such income as W-2 income identified.','Identify Schedule K participants receiving income as W-2 and place W-2 amount on census.','Schedule K passing through as W-2 income not applicable.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 67,'Are all participation agreements in place for all participating employers, especially if the sponsor is a partnership or sole proprietorship?', 'Participation agreements in place for all participating employers.','Provide participating agreements or remove money contributed by non-participating employers. Seek advice of consulting.','Participation Agreements not applicable.','help_text','https://www.youtube.com','category',false),
('client compliance guide', 68,'Has all the income for employees been accounted for or have you explained who has not on tab 2?', 'All income provided. Matches W-3.','Add all employee information so that gross compensation matches W-3.','Please anwer yes or no as to whether all income was provided. The answer cannot be not applicable.','help_text','https://www.youtube.com','category',false);

# Create some dummy checklists for the two templates for the preparer - let's say 3 each for a total of 6 - not started, in progress and complete

# have preparer answer with a mix showing incomplete which will produce Kanban

#2.0 
# query for returning Kanban lists, counts, percents

# have preparer answer with a mix that will show all complete

# query for returning Kanban lists, counts, percents - ready for review look

# 1.0
# have preparer enter send to reviewer the 2 complete and mark one for return and one ready.

# have reviewer answer with a mix showing incomplete which will produce Kanbans

# have reviewer enter returned for corrections

# have reviewer answer with a mix that will show all complete - ready for recipient look

# have reviewer enter sent to recipient

# 2.0
# reviewer Kanbans

# 3.0

# sql queries that will illustrate stats

# sql queries specifically on questions marked for review at any time

# once complete move on to convert to SQLAlchemy for web page display/ receipt of web input
