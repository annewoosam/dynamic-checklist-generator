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
                     primary_driver BOOLEAN NOT NULL
                     );

CREATE TABLE checklist (
                     checklist_id SERIAL PRIMARY KEY,
                     template_name VARCHAR NOT NULL,
                     timeframe DATE NOT NULL,
                     who_for VARCHAR NOT NULL
                     );
CREATE TABLE answers (
                     checklist_id INTEGER,
                     answer_id SERIAL PRIMARY KEY,
                     question_number INTEGER,
                     role BOOLEAN,
                     answer VARCHAR,
                     time_spent INTEGER,
                     comment VARCHAR
                     );
CREATE TABLE notifications (
                     notifications_id SERIAL PRIMARY KEY,
                     date_sent_to_review DATE,  
                     reviewer_full_name VARCHAR,
                     reviewer_email VARCHAR,
                     date_review_completed DATE,   
                     recipient_full_name VARCHAR,
                     recipient_email VARCHAR, 
                     date_sent_to_recipient DATE
                     );
CREATE TABLE corrections (
                     corrections_id SERIAL PRIMARY KEY,
                     question_number INTEGER,
                     role BOOLEAN,
                     answer VARCHAR,
                     date_registered DATE
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
('compliance testing', 2, '2. Has the questionnaire been received?', 'Questionnaire received.','Questionnaire not received. Request. If the client appears to answer the same way each year move forward and ask the client to send a Questionnaire, confirm results.','A Questionnaire should be provided. If the client appears to answer the same way each year move forward and ask the client to send a Questionnaire, confirm results.','If the questionnaire is missing, prepare as much of the testing as possible based on assumptions inherited from the prior year, using either the system. E-mail the relationship manager: I am proceeding based on the prior year questionnaire. That said I cannot release the results until I have received the questionnaire for the current year.','https://www.youtube.com','QUESTIONNAIRE',false),
('compliance testing', 3, '3. Is the census formatted in a format that can be directly loaded into the system?', 'Census is in a format ready for load.','Census must be formatted before it can be loaded.','An invalid response for whether the census was formatted correctly was entered. Choose either Y or N.','If the census has critical errors that prevent you from loading it into the system, let the relationship manager know. Some sample language: The census does not have social security numbers. The census is missing compensation for some employees. The census is missing compensation for all employees. The census is missing hours for some employees and the plan requires hours to calculate eligibility/allocate a contribution.','https://www.youtube.com','CENSUS',false),
('compliance testing', 4, '4. Has the census been loaded to the system?', 'Census loaded.','Census must be formatted before it can be loaded.','An invalid response for whether the census was loaded was entered.  Choose either Y or N.','Make sure to load the census into the system and perform all necessary data checks within the system and forward all questions to the relationship manager. Review against the Eligibility Proof','https://www.youtube.com','CENSUS',false),
('compliance testing', 5, '5. Has an Eligibility proof been prepared from the census that separates employees into the categories HCEs, NHCEs, Ineligibles(with explanation such as age,service), Excluded, Prior Year Terms?', 'Eligibility Proof employee classifications have been made.','Eligibility Proof employee classifications need to be made.','An invalid response for the Eligibility Proof employee classification step was entered. Choose either Y or N.','Use the template for the eligibility proof to estimate the test results. Formulas are included in the proof.','https://www.youtube.com','ELIGIBILITYPROOF',false),
('compliance testing', 6, '6. Does the proof indicate the HCEs percentages, relationships and attribution for all employees with the same name as owner-employees, those earning over $120,000 in a prior year?', 'Owner percentages, relationships for those with the same last name as the owners and other relatives, and persons making over $120,000 in the last year have been marked in the file.','Census must be formatted before it can be loaded.','No valid response entered Enter Y, N or NA to indicate whether all owner percentages, relationships for those with the same last name as the owners and other relatives, and persons making over $120,000 in the last year have been marked in the file.','Enter the HCE percentages, relationships and attribution on the Eligibility proof. If you had to use prior year note that and add a request for confirmation to your questions.','https://www.youtube.com','HCE',false),
('compliance testing', 7, '7. Does the proof indicate the estimated Actual Deferral Percentage and properly cap the deferrals and the compensation considered at the at the limit for the year tested?"', 'Preliminary ADP ACP Results have been calculated and compared to the reports generated by the system. Variances have been resolved.','Update the file with owner percentages, mark family with a 1 in the family/spouse/lineal descendant area or potential family relationships with a Y or N and flag persons making over 120,000 in the prior year with a Y as needed.','This plan does not have deferrals or match. ADP ACP testing does not apply','The Eligibility Proof contains instructions on how to determine the HCEs using ownership and attribution, as well as compensation and to apply the Top Paid Group election as needed. Make sure you sort employees into their eligibility classifications such as HCE versus NHCE, ineligible and excluded. Also, make sure you apply the compensation and deferral limits and factor-out any catch-up contributions in calculating the parentage of compensation each person deferred and the average deferral percentage for the HCE and NHCE groups.','https://www.youtube.com','ADP',false),
('compliance testing', 8, '8. Have you indicated whether the plan uses Prior Year Testing and confirmed that the system is correctly set-up for Prior Year Testing?', 'The Prior Year Testing numbers have been entered.','Preliminary ADP ACP Results have NOT been calculated and compared to the reports generated by the system. OR Variances have been resolved.','The plan does not use prior year testing.','The plan document will tell you whether the plan uses Prior Year testing or not. Obtain the percentages you use from the prior year’s ADP and ACP testing. If the plan is using the prior year testing method for the first time, use 3%. Note that a plan could use prior year testing for one source and not the other and rarely, some groups may be using prior and others could be using current so a location based testing method may need to be used to track the prior year percentages appropriately.','https://www.youtube.com','PRIORYEAR',false),
('compliance testing', 9, '9. Have you confirmed the formula for any Match and ensured it is entered in the testing system? Enter NA if the plan either does not have a match source or will not be funding a match this year.', 'Match formula confirmed and entered and results checked.','Enter the match formula into the system after confirming it against the document/client questionnaire/prior practice. If using a prior formula, indicate in Results sent to client.','The plan does not have a match source or is not funding the match this year.','The match formula will be stated in the plan document. You should also notate this formula on the Eligibility proof and perform a manual check and do a common sense comparison to last year’s funding amount, especially if the plan is new to your testing system.','https://www.youtube.com','MATCH',true),
('compliance testing', 10, '10. Have you confirmed the formula for any Safe Harbor Match and ensured it is entered in the testing system?', 'Safe Harbor match formula confirmed and entered and results checked.','The plan does not have a Safe Harbor match source or is not funding the match this year.',' No valid response entered. Please enter a Y,N or NA as to whether the plan uses a Safe Harbor match and you have entered the formula into the system and checked the calculation.','The Safe Harbor match formula will be stated in the plan document. You should also notate this formula on the Eligibility proof and perform a manual check and do a common sense comparison to the prior year funding amount, especially if the plan is new to your testing system. The most common formula is 100% to 3% and 50% to 5% of compensation and the Eligibility proof will explain how to confirm this. Note that sometimes there are maybe provisions for Safe Harbors. If a plan has a maybe provision noted in the plan document, you will need to have the annual amendment stating that the Safe Harbor will be funded to use this method to pass testing.','https://www.youtube.com','SAFEHARBORMATCH',false),
('compliance testing', 11, '11. Have you verified the Match if the plan requires calculation and is on an annual basis according to the plan document/adoption agreement?', 'Match basis has been checked and whether a calculation is required was verified.','Match basis (annual or not) or whether a calculation is needed must be verified.','There is no Match source or the match is not being funded this year.','Verify the match by downloading the trust statement to csv format and using vlookup in a spreadsheet to find any differences in what was funded and what is being calculated when a plan’s adoption agreement states that the funding is on an annual basis. If the funding is not on an annual basis, simply verify that the funding did not exceed the formula. If there is a variance, check to confirm that the information is not funding that is from a prior year due to timing differences before checking with the client/creating a true-up file.','https://www.youtube.com','MATCH',false),
('compliance testing', 12, '12. If the plan is a sole proprietorship or partnership and has Schedule C or Schedule K income that is not passing through as W-2 income, has the owner/all partners signed participation agreements?', 'All participation agreements for participating employers signed.','Participating agreements missing/amendment and filing required.','Participation agreements do not apply to this plan.','The plan document and questionnaire will indicate of a plan is a sole proprietorship or partnership. Be aware that some sole proprietorships/partnerships use pass their income through as W-2 wages, in which case, it is not necessary to make adjustments for schedule C or K income. If a sole proprietor or partner is participating make sure they have signed any necessary participation agreements.','https://www.youtube.com','category',false),
('compliance testing', 13, '13. Has the income for sole proprietors/partners been entered correctly based on either Draft or final Schedule C or K-1 documents? Search for Entity Type in the plan document/adoption agreement to identify if the plan is a sole proprietorship/partnership not taxed as a corporation.', 'Schedule C or K income entered completely on file and draft or final schedules provided.','Provide Schedule C or K income and draft or final schedules.','The plan is not a sole proprietorship or a partnership. Therefore Schedule C or K income does not have to be provided.','The plan document and questionnaire will indicate of a plan is a sole proprietorship or partnership. Be aware that some sole proprietorships/partnerships use pass their income through as W-2 wages, in which case, it is not necessary to make adjustments for schedule C or K income. If a sole proprietor or partner is participating make sure they have signed any necessary participation agreements','https://www.youtube.com','K1',false),
('compliance testing', 14, '14. Did you load and generate the ADP and ACP Tests?', 'ADP ACP tests generated.','Generate ADP ACP tests.','The plan does not have deferrals/match.','ADP tests would not be required if no deferrals were made or under most circumstances where a plan is a 403(b) plan. ACP tests would not be required if there was no match. Note that if a plan has a Safe Harbor match and a regular match and contributes to both, the regular match is subject to an ACP test.','https://www.youtube.com','ADPACP',false),
('compliance testing', 15, '15. Do the ADP and ACP tests match your expectations on the proof or if not have you explained the differences and made the adjustments needed to tie out the system to the census?', 'ADP and ACP tests match expectations based on proof/prior testing review.','ADP and ACP tests do not match expectations based on proof/prior testing review.','The plan does not have deferrals/match.','When the ADP and ACP tests do not match expectations, identify the amount off and see if one person matches that amount; if not export the test data including name and contribution with a unique identifier such as social security number that can be vlooked up against or join the names to create a unique identifier and perform a vlookup in both directions, if needed. Then, after the persons identified as dropped from the report or with numbers in error show up. Some possible tactics to determine why there is an issue: confirm eligibility, any classifications such as exclusions that may be inherited from the prior year but may have changed the current testing year, or the possibility that the person was rehired and came in immediately to the plan as a start.','https://www.youtube.com','ADPACP',false),
('compliance testing', 16, '16. Has all the income for employees been accounted for?', 'All employee income accounted for.','Employee income appears to be missing. Contact client.','Not a valid response. Enter Y or N as to whether all employee income is accounted for.','All income should be accounted for. If income has dropped, confirm that the income is not too high for the system to register it and that the system is properly handling Schedule C and K1 reductions. Generally a report can be printed to show how the system is reducing for Schedule C and K1 reductions.','https://www.youtube.com','INCOME',false),
('compliance testing', 17, '17. Did the client provide excluded compensation for the Match calculation?', 'Excluded Compensation was provided for the match.','Excluded Compensation needed for the match. Contact client.','There is no excluded compensation for the match or the match is not being funded or the plan does not have a match source.','If the client failed to provide excluded Match compensation add to your questions to client: Please provide the compensation which should be excluded from the match calculation according to your plan document. List the type of compensation.','https://www.youtube.com','MATCH',false),
('compliance testing', 18, '18. Have you checked for plan Match excesses if the plan Match is on an allocation or payroll period basis?', 'Match excess checked.','Check for Match excesses.','Match excesses do not need to be checked because there is no match or the plan match is now being calculated and has not been funded yet.','Only register cases in which the client overfunded the match unless there is a significant variance. If there is a significant variance, check first whether the prior year’s match data may be being used for some or all of the people.','https://www.youtube.com','MATCH',false),
('compliance testing', 19, '19. Have you prepared the Match Contribution file for either the contribution/calculation or excesses?', 'The match file has been prepared.','The Match file needs to be prepared.','Not applicable. No match is being funded or the match funded is the same as that confirmed by the system.','Prepare the Match Contribution file, indicating funded amounts and the difference to fund, if some funding has already been received.','https://www.youtube.com','MATCH',false),
('compliance testing', 20, '20. Did the client provide the formula and classes for the Profit Sharing or Nonelective calculation? Enter N if the client was undecided. Enter NA if no Profit Sharing source or contribution to be made.', 'The Profit Sharing/Nonelective formula was provided or is specified in the document.','The Profit sharing/nonelective formula must be obtained from the plan sponsor.','The Profit Sharing/nonelective formula is not needed because the source does not apply to this plan or the source will not be funded this year.','If the client failed to provide the formula and classes, add to your questions to the client: I understand that you intend to fund a cross-tested Profit Sharing contribution to your employees this year. In order to create the allocation, I need you to update the file to include the classes(group) for each employee and a formula to apply, as well as any budget caps you want to use. You may submit additional scenario requests in the same file.','https://www.youtube.com','PROFITSHARING',true),
('compliance testing', 21, '21. Did the client provide excluded compensation for the Profit Sharing or Nonelective calculation?', 'Excluded compensation was provided.','Excluded compensation must be provided.','Excluded compensation is not allowed in this plan.','If the client failed to provide the formula and classes, add to your questions to the client: I understand that you intend to fund a cross-tested Profit Sharing contribution to your employees this year. In order to create the allocation, I need you to update the file to include the classes(group) for each employee and a formula to apply, as well as any budget caps you want to use. You may submit additional scenario requests in the same file.','https://www.youtube.com','PROFITSHARING',false),
('compliance testing', 22, '22. If the plan is cross-tested, that is, every individual is in their own class and is making a Profit Sharing/Nonelective contribution have you confirmed the formula calculations?', 'Profit Sharing/Nonelective calculations have been confirmed.','Profit Sharing/Nonelective calculations must be confirmed.','Profit Sharing/Nonelective Calculations do not apply because the source is not permitted or because no funding will be made this year.','Confirm the formula calculations within the Eligibility Proof. Account for any K-1/Schedule C adjustments to income and for contributions as a percent of ownership and show any classes used in the calculation. Show that the formula matches the reports or adjust either the system or spreadsheet as appropriate.','https://www.youtube.com','PROFITSHARING',false),
('compliance testing', 23, '23. Have you prepared the Profit Sharing/Nonelective Contribution file for either the contribution/calculation or excesses?', 'Profit Sharing/nonelective contribution file prepared.','Profit Sharing/nonelective contribution file must be prepared.','No Profit Sharing/Nonelective file is required as the source does not exist or there will be no funding this year.','Prepare the file showing either the entire contribution due, as well as the percentage of compensation being contributed and the relevant data needed by operations to load the file (social security number, dates, name and source and contribution amount).','https://www.youtube.com','PROFITSHARING',false),
('compliance testing', 24, '24. Have you confirmed that HCEs by Attribution are identified in the file?', 'Owner family members and persons with same last name as owners have relationship to owners identified.','Identify owner family members and relationship to owners of people with the same last name.','No owners in the plan.','If the attribution was not confirmed by the current questionnaire then state that in the Assumptions used. Sample text: I used last year’s information to determine owners by attribution because no updated information was provided for this year. If any owners by attribution are no longer owners by attribution, please let me know so that I can recalculate and reprint the reports.','https://www.youtube.com','ATTRIBUTION',false),
('compliance testing', 25, '25. Did you load the participant source activity?', 'Participant contribution by source loaded.','Participant contribution by source must be loaded.','There is no participant contribution activity to load.','Obtain the participant source activity and format it as needed from the recordkeeping system reports portal/interface.','https://www.youtube.com','ACTIVITYLOAD',false),
('compliance testing', 26, '26. Have you printed the Top Heavy Test for next testing year and the current allocation if the plan is not a 100% Union or 403(b) plan and one of the following situations apply: The plan is receiving (1) Deferrals only, (2) Deferrals and Match only or (3) Deferrals and a Safe Harbor contribution and is making Profit Sharing/Nonelective contributions?', 'Top Heavy Allocation & Test Printed.','Print Top Heavy Allocation & Test.','Top Heavy Allocation & Test do not apply.','To properly perform a Top Heavy Test make sure that the plan’s owners are correctly identified including percent of ownership in all cases. For the Top Heavy test you must also confirm that the officers are correctly coded in the system. If no officers are listed AND there are individuals making over $150,000 as indexed AND these individuals are not already classified as owners, add a question to client: Please confirm the following persons are not officers:','https://www.youtube.com','TOPHEAVYTEST',false),
('compliance testing', 27, '27. Did you load vesting?', 'Vesting loaded.','Load vesting.','Vesting load does not apply.','Obtain the vesting report from the recordkeeping system reports portal/interface, format it as needed and load it.','https://www.youtube.com','VESTINGLOAD',false),
('compliance testing', 28, '28. Did you confirm census contributions against the trust and provide a true-up file for any variances?', 'Trust accounting complete.','Complete trust accounting.','Trust accounting does not apply.','Download an excel or csv file of the activity from the recordkeeping on a payroll basis and obtain the same in excel or csv if possible from the trust(custodian). Use vlookup to identify any errors. If needed use printing reports in 1/2 timeframes to narrow down the timeframe for any variances so you can research transactions causing.','https://www.youtube.com','TRUEUP',false),
('compliance testing', 29, '29. Has the client responded to all questions?', 'Client has responded to all questions.','Follow-up with client on questions.','Client questions do not apply.','If not, follow-up with the relationship manager every two days. Response time can easily delay testing two weeks or more when not frequently managed.','https://www.youtube.com','CLIENTRESPONSES',true),
('compliance testing', 30, '30. Have all the client responses been entered?', 'Client responses all entered.','Enter client responses.','Client responses not applicable.','Enter the responses as soon as possible.','https://www.youtube.com','CLIENTRESPONSES',false),
('compliance testing', 31, '31. Have you regenerated the reports and re-confirmed the numbers?', 'Reports reprinted and re-reconciled.','Reprint reports and re-reconcile.','Reprinting reports and re-reconciling not applicable.','help_text','https://www.youtube.com','REGENERATE',false),
('compliance testing', 32, '32. Did you print the Title Page?', 'Title page printed.','Print title page.','not_applicable-text','Regenerate all reports and re-reconcile all worksheets as soon as possible so that the package can be sent into review.','https://www.youtube.com','TITLEPAGE',false),
('compliance testing', 33, '33. Did you print the Table of Contents?', 'Table of contents printed.','Print table of contents.','Title page is not applicable.','Not all plans/blocks require title pages. Some may require branding.','https://www.youtube.com','TABLEOFCONTENTS',false),
('compliance testing', 34, '34. Did you print the Results Summary?', 'Results summary printed.','Print results summary.','Table of contents not applicable.','Not all plans/blocks require a table of contents.','https://www.youtube.com','RESULTS',false),
('compliance testing', 35, '35. Did you print the ADP and ACP Nondiscrimination Test or ADP Nondiscrimination Test, as applies?', 'ADP/ACP report printed.','Print ADP/ACP report.','not_applicable-text','Use the results summary format that applies to the plan/block you are working on.','https://www.youtube.com','ADPACP',false),
('compliance testing', 36, '36. Did you print the Catch-Up Contributions Summary?', 'Catch-Up contribution report printed.','Print Catch-up contribution report.','Catch-up contribution report does not apply','The ADP or ACP tests may be irrelevant if the plan had no deferrals or match funded or as a source.','https://www.youtube.com','ADPACP',false),
('compliance testing', 37, '37. Did you print the Annual Additions Test?', 'Annual Additions report printed.','Print Annual Additions report.','Annual Additions report not applicable.','The annual additions test is also known as the 415 test and alows for contribution no greater than the amount stated by law for the year involved or 100% of compensation, whichever is least.','https://www.youtube.com','ANNUALADDITIONS',false),
('compliance testing', 38, '38. Did you print the General Test under 401(a)(4)?', 'General Test printed.','Print General Test.','General test does not apply.','If the plan is not funding Profit Sharing or a Nonelective contribution or the contribution is integrated or a flat percentage of compensation or based on a nondiscriminatory age or service formula the test does not need to be generated.','https://www.youtube.com','PROFITSHARING',false),
('compliance testing', 39, '39. Did you print the Budget Report for Sole Proprietorships/Partnerships with Schedule C or K income?', 'Budget printed.','Print Budget.','Budget does not apply.','The budget report will show the reductions for FICA and contributions to rank and file employees and their impact on how much the sole proprietors/partners can contribute when these amounts are factored in.','https://www.youtube.com','K1',false),
('compliance testing', 40, '40. Did you print the 414(s) test if excluded compensation other than 125, reimbursements or date of participation compensation was used?', '414(s) printed.','414(s) not printed.','414(s) does not apply.','414(s) tests are rarely run but become neccessary when a plan makes contributions based on excluded compensation other than those in the 125 plan and reimbursements and compensation earned after entering the plan. Excluding commissions and bonuses will trigger the test.','https://www.youtube.com','414S',false),
('compliance testing', 41, '41. Did you place a copy of the census in the working papers folder, all review files in the Review Folder and all Client Files including reports and contribution and refund files in the Client Folder?', 'Files saved to folders.','Save files to folders.','Saving files to folders does not apply.','All files should be saved in teh appropriate folders. Use an archive folder if you are unsure whether you might need to revert back to an older version of testing then delete the folder when the approved files have been delivered to the recipient.','https://www.youtube.com','FILES',false),
('compliance testing', 42, '42. Did you enter the contributions for deferrals and roth for the three relevant periods as necessary if the plan is an Off-Calendar (fiscal year end) plan?', 'Off-calendar 402(g) numbers entered.','Enter off-calendar 402(g) numbers.','402(g) numbers do not apply.','Obtain the necessary contribution amounts per person per source for 3 periods - 1/1 to the plan year end in the prior year; the first day of the plan year to 12/31 of the plan year end in the prior year. 1/1 of the current year to the plan year end.','https://www.youtube.com','OFFCALENDAR',false),
('compliance testing', 43, '43. Did you update vesting to 100% if the plan terminated and has a signed termination agreement and did you adjust the testing compensation by the ratio of months in the plan year based on the year end date?', 'Plan Termination vesting updated.','Update vesting for plan termination.','Plan is not terminating - vesting update to 100% not applicable.','If the plan is terminating you will need to update the vesting to 100% for all participants. When the termination rate is 20%+ there may be a need to vest all partipants terminated that year 100% Cases where 20%+ of employees have been terminated during the year should be referred to consulting.','https://www.youtube.com','PLANTERMINATION',false),
('compliance testing', 44, '44. For plans with Short Plan Years did you adjust the testing compensation, the deferral limits and any required hours for testing?"', 'Short Plan Year compensation, deferral limits and hours adjustments made.','Make adjustments to compensation limit, deferral limit and hours for short plan year.','Short plan year adjustments not applicable.','Use a ratio to prorate hours based on how much of the plan year lapsed from the beginning of the plan year to the end of the plan year based on the termination date adopted in the signed amendment.','https://www.youtube.com','SHORTPLANYEAR',false),
('compliance testing', 45, '45. Has the relevant tracking database been updated?', 'Tracking database updated.','Update tracking database.','Tracking database update not applicable.','Tracking databases could range from spreadsheets to customer relationship management software and might include a mix. Make sure you unerstand what tracking is used and under what circumstances. For example, all plans might be tracked in a database but only some on a spreadsheet - perhaps only those being billed for test failures, consulting issues, profit sharing calculations or special projects such as mid-year testing and projections, late deferrals or missed deferral opportunities.','https://www.youtube.com','TRACKING',false),
('compliance testing', 46, '46. If the plan had late deferrals, have you logged a request to prepare a submission in the relevant tracking database?', 'Late deferrals tracking record created.','Log a late deferrals tracking record.','A late deferrals tracking record is not needed.','Late deferrals are generaly flagged by clients in questionnaires but may also appear as reconciling items when the trust accounting is performed.','https://www.youtube.com','LATEDEFERRALS',false),
('compliance testing', 47, '47. Have you logged a request to begin preparation of the 5500, Summary Annual Report and 8955-SSA in the relevant tracking database?', 'Government Forms Tracking created.','Add Government Forms tracking.','Government Forms tracking is not needed for this plan.','Know what processes need to be logged to get the government forms generated, reviewed and sent to the client for signature.','https://www.youtube.com','GOVERNMENTFORMS',false),
('client compliance guide', 48, '1. Is your file organized with the same top row as the initial file downloaded?', 'Headers fine.','Fix headers.','We assumed headers do not apply to your file. It is a custom file. This will likely slow down processing because the file will need to be manually formatted instead fo automatically processed.','Not providing a file which is correctly arranged can result in delays and errors in your testing.','https://www.youtube.com','HEADERS',false),
('client compliance guide', 49, '2. Apply a filter across the rows in the original template. When you filter social security numbers are there any blanks?', 'Social Security Numbers fine.','Fix social security numbers.','You answered N/A. We can use employee ID numbers to load a file when social security numbers are not available. All employees must have employee IDs in order to link their information from year to year and avoid confusion when employees have similar names.','Social security numbers or another unique identifier such as an employee id are needed to match data for employees from year to year. You can transmit your files securely.','https://www.youtube.com','SSN',false),
('client compliance guide', 50, '3. When you filter dates of birth are there any blanks?', 'Dates of Birth Fine.','Fix Dates of Birth.','Warning! All files should have dates of birth.','Dates of birth are used to determine eligibility and entry for a plan. Unless the plan has no age requirement and is a Safe Harbor or has no HCE contributions it is expected that these will be provided so that test results can be accurately calculated.','https://www.youtube.com','BIRTH',false),
('client compliance guide', 51, '4. When you filter dates of birth are there any for persons under 18', 'Dates of birth for young employees are correct.','Fix dates of birth for employees that make them younger than they are.','No employees are under 18.','Sometimes persons under 18, expecially owners children may be hired as teenagers and flagged in the system for extra scrutiny. Other times they may be indicators of a typing error.','https://www.youtube.com','BIRTH',false),
('client compliance guide', 52, '5. When you filter dates of birth are there any for persons over 80 who should not be', 'Retiree dates of hire fine.','Fix dates of birth for retiree hires.','There are no retiree age hires.','Some testing systems will flag anyone over retirement age for review. Please ensure these persons birthdates are correct','https://www.youtube.com','BIRTH',false),
('client compliance guide', 53, '6. When you filter dates of hire are there any blanks', 'Dates of Hire fine.','Fix dates of hire.','All employees must have a valid date of hire. Correct the file and change your answer to Y.','All employees must have a valid date of hire so that we can accurately calculate their eligibility for the plan and entry date, as well as the vesting of their contributions. After testing is complete, the next step in annual administration is government forms filing, which includes the tracking and reporting of the numbers of persons with balances not 100% vested using the Form 8955-A.','https://www.youtube.com','HIRE',false),
('client compliance guide', 54, '7. Are there any blank dates of rehire for persons who have a termination date prior to this year and received compensation?', 'Dates of Rehire fine.','Fix dates of rehire.','Dates of rehire did not apply.','Inaccurate dates of rehire can make someone drop from the tests, causing results to be inaccurate. When the ADP test is inaccurate and discovered after the refund deadline, penalties may apply.','https://www.youtube.com','REHIRE',false),
('client compliance guide', 55, '8. Are there any termination dates for people before rehire dates?', 'Dates of rehire after termination fine.','Fix dates of rehire.','There are no dates of rehire to correct.','Termination dates after rehire dates may cause someone to drop from the tests in error','https://www.youtube.com','REHIRETERM',false),
('client compliance guide', 56, '9. When you apply a filter do you have percentages in the ownership column that add up to 100% or is not have you explained on tab 2?', 'Owners identified.','Enter owner percentages onto the file.','If there are no owners, note on tab 2.','All ownership nmust be accounted for or teh tests may be inaccurate and a plan may fail the ADP test but the discovery may be too late to correct the test without causing penalties for late compliance. There are some circumstances where a plan may truly have outside non-employee ownership, which causes the ownership percentages to be less than 100%, but this tends to be rare.','https://www.youtube.com','OWNERSHIP',false),
('client compliance guide', 57,'10. Have you placed a Y in the officer column for each officer or explained on tab 2 that there are no officers', 'Officers have been marked in the file.','Mark officers.','No officers are employees.','Officers must be identified so that the top heavy test and allocation can be performed accurately. If a plan has no persons earning over $150,000 as indexed there will be no officers of concern for the test. Of, however, the plan does have officers earning over $150,000, not flagging them could cause a test failure to be discovered later, with consequences for the plan.','https://www.youtube.com','OFFICERS',false),
('client compliance guide', 58,'11. Have you indicated the relationship of all family members for anyone who has a relationship to the owner(s)?', 'Family attribution has been noted in the file, including for persons with the same last names as the owners.','Fix family attribution including noting relationship of persons with the same last name as the owners.','There is no ownership in this plan or persons with the same last name as the owners','If family attribution is not correctly identified, the HCEs may be improperly determined and a plan might pass a test it should be shown as failing with penalties if the correction is late. One of the most common attribution errors is attributing ownership to siblings (borthers or sisters). While there is no attribution between siblings it is good to notate these relationships to prevent delays in processing while waiting for clarification of these relationships.','https://www.youtube.com','ATTRIBUTION',false),
('client compliance guide', 59,'12. Have you entered a formula for the Match or entered no match on tab 2?', 'Match contributions clarified - either none or for yes, formula and principal class numbers and budget provided.','Provide match answer and formula if funding.','Match does not apply.','Your plan document will indicate whether or not the plan has a match source. If it does and the match is fixed, you are good to go. If it does not mark n/a. If it does have a match but the formula is discretionary, generally in the absence of guidance, you will be provided a match with the prior year formula if you did not specify the formula, given the volume of plans processed.','https://www.youtube.com','MATCH',false),
('client compliance guide', 60,'13. Have you entered a formula for Profit Sharing including the class of each person based on how much Profit Sharing they should receive if eligible in the Principal column?', 'Profit sharing/nonelective contributions clarified - either none or for yes, formula and principal class numbers and budget provided.','Provide Profit Sharing formula, and if, each class is its own separate group in the plan document(adoption agreement), add a principal code column to your spreadsheet and enter the group number to use for each eligible individual. On tab 2 identify the target percentage or dollar amount for each group or the plan as a whole.','"Profit Sharing or nonelective contributions will not be made for this testing year.','Your plan document will indicate whether or not the plan has a profit sharing or nonelective source. If it does and the profit sharing is fixed, you are good to go. If it does not mark n/a. If it does have a profit sharing/nonelective source but the formula is discretionary, generally in the absence of guidance, you will be provided with a contribution calculation with the prior year formula(s) if you did not specify the formula(s), given the volume of plans processed.','https://www.youtube.com','PROFITSHARING',false),
('client compliance guide', 61,'14. Excluded Compensation must be excluded in the plan document to be disregarded in calculating the Match/Profit Sharing. Have you confirmed that you did not enter the same amount as the compensation for participants not yet eligible to participate in the plan?', 'Excluded compensation provided.','Provide excluded compensation.','No excluded compensation is permitted in the plan document(adoption agreement) or the plan can use excluded compensation but chooses not to and is passing all tests and not funding any employer contributions such as a match or profit sharing or nonelective contribution, whether regular or Safe Harbor.','A plan may be tested without excluding compensation that is listed in the plan document as excluded from a source or sources. If it passes, all is well. If, however, it fails, the plan may be tested with excluded compensation to see if it passes. So providing excluded compensation can be useful. Note that plan contributions may also have to be calculated using excluded compensation. Depending on the type of excluded compensation, (compensation that is not date of participation compensation or cafeteria plan contributions, for example) an additional test, the 414(s) compensation test may have to be run to confirm that the compensation can be excluded from calculating the contribution per IRS non-discrimination guidelines.','https://www.youtube.com','EXCLUDEDCOMPENSATION',false),
('client compliance guide', 62,'15. Excluded Employees must be excluded in the plan document to be disregarded in testing. Have you marked all these employees with a Y?', 'Excluded employees marked - fine.','Mark excluded employees.','There were no excluded employees.','Employees may be excluded by class, which may help plans pass testing. Note that special rules apply to part-time and union employee exclusions, among others.','https://www.youtube.com','EXCLUDEDEMPLOYEES',false),
('client compliance guide', 63,'16. If your plan transferred to us in the middle of the plan year, did you provide the prior testing results?', 'Prior testing results provided.','Prior testing results need to be provided.','Prior testing results do not need to be provided because the plan was tested at the current provider last year or the first testing year is this year.','Providing prior year testing helps quickly establish if ineligible employees are actually eligible, helps fill in data missing from the census without back and forth, and provides a cross-check aganst the current testing year results and contribution funding. These results should always be provided as soon as possible.','https://www.youtube.com','TAKEOVERPLAN',false),
('client compliance guide', 64,'17. If your plan transferred to us in the middle of the plan year, did you provide the prior custodian statement of contributions by participant by money type(source)?', 'Prior contribution data was provided.','Provide prior contribution information.','All activity for the testing year was conducted at the same provider. There were no conversions from another provider or outside accounts.','Providing prior provider contribution data quickly allows us to identify any contribution errors as soon as possible, minimizing the cost of late funding penalties.','https://www.youtube.com','TAKEOVERPLAN',false),
('client compliance guide', 65,'18. If your entity is a Sole Proprietorship or Partnership have you entered Schedule C or Schedule K income on the spreadsheet and provided draft or actual Schedules?', 'Schedule C or K income entered comepletely on file and draft or final schedules provided.','Provide Schedule C or K income and draft or final schedules.','The plan is not a sole proprietorship or a partnership. Therefore Schedule C or K income does not have to be provided.','Sole proprietorships and parnerships that are not receiving pass-through W-2 income must have their income reduced for FICA and contributions to employees in calculating contributions.','https://www.youtube.com','K1',false),
('client compliance guide', 66,'19. Have you identified any Schedule K recipients who are actually receiving income as W-2 income?', 'Schedule K participants receiving such income as W-2 income identified.','Identify Schedule K participants receiving income as W-2 and place W-2 amount on census.','Schedule K passing through as W-2 income not applicable.','Occasionally sole proprietorships and partnerships or individual members thereof receive their income as pass-through W-2 income. Specifiying if this applies to the plan, who to and ensuring that the appropriate participation agreements or amendments are in place up front will reduce the need to re-calculate tests and contributions.','https://www.youtube.com','K1',false),
('client compliance guide', 67,'20. Are all participation agreements in place for all participating employers, especially if the sponsor is a partnership or sole proprietorship?', 'Participation agreements in place for all participating employers.','Provide participating agreements or remove money contributed by non-participating employers. Seek advice of consulting.','Participation Agreements not applicable.','Having all participation agreements in place or amendents drafted and adopted timely will reduce time and effort re-calculating tests and contributions. Partnerships and certain industries such as medical and investment companies, as well as law offices should ensure that they have correctly provided these documents.','https://www.youtube.com','PARTICIPATIONAGREEMENTS',false),
('client compliance guide', 68,'21. Has all the income for employees been accounted for or have you explained who has not on tab 2?', 'All income provided. Matches W-3.','Add all employee information so that gross compensation matches W-3.','Please anwer yes or no as to whether all income was provided. The answer cannot be not applicable.','If there is missing income, it may affect the testing results and contribution calculations. Using a cross-check against the W-3 also ensures that no potentially eligible participants have been dropped, decreasing the chance of having persons with missed deferral opportunities that need to be funded by the plan sponsor.','https://www.youtube.com','ALLINCOME',false);

-- # Create some dummy checklists for the two templates for the preparer - let's say 3 each for a total of 6 - not started, in progress and complete

-- # have preparer answer with a mix showing incomplete which will produce Kanban
-- check with
-- dropdb checklists
-- createdb checklists
-- psql checklists < database.sql
-- psql checklists
-- can use \dt or \d and also \q for quit before reunning queries

-- retrieve all questions reqgardless of template name

-- # SELECT question, help_text, resource_url, primary_driver, category FROM template_questions

--retrieve questions by template/cross-check against number expected. Any updates made should also be made in parallel json file. Also avoid possessiveness :) ' versus ""

-- # SELECT question FROM template_questions WHERE template_name='compliance testing';      --47 rows return
-- # SELECT question FROM template_questions WHERE template_name='client compliance guide'; --21 rows return

--retrieve question and text of different categories for review by template

-- HELP TEXT

-- # SELECT question, help_text FROM template_questions WHERE template_name='compliance testing';      --47 rows return
-- # SELECT question, help_text FROM template_questions WHERE template_name='client compliance guide'; --21 rows return

-- VIDEO-TEXT AKA RESOURCE_URL
-- # SELECT question, help_text FROM template_questions WHERE template_name='compliance testing';      --47 rows return
-- # SELECT question, help_text FROM template_questions WHERE template_name='client compliance guide'; --21 rows return

-- CATEGORIES
-- # SELECT question, help_text FROM template_questions WHERE template_name='compliance testing';      --47 rows return
-- # SELECT question, help_text FROM template_questions WHERE template_name='client compliance guide'; --21 rows return

-- DRIVERS
-- # SELECT question, help_text FROM template_questions WHERE template_name='compliance testing';      --47 rows return
-- # SELECT question, help_text FROM template_questions WHERE template_name='client compliance guide'; --21 rows return



-- #2.0 

-- # query for returning Kanban lists, counts, percents

-- FOR KANBAN
--First check all your text
-- YES-TEXT
-- # SELECT question, yes_text FROM template_questions WHERE template_name='compliance testing';      --47 rows return
-- # SELECT question, yes_text FROM template_questions WHERE template_name='client compliance guide'; --21 rows return

-- NO-TEXT
-- # SELECT question, no_text FROM template_questions WHERE template_name='compliance testing';      --47 rows return
-- # SELECT question, no_text FROM template_questions WHERE template_name='client compliance guide'; --21 rows return

-- NOT_APPLICABLE TEXT
--some items around 34 need to be fixed
-- # SELECT question, not_applicable_text FROM template_questions WHERE template_name='compliance testing';      --47 rows return
-- # SELECT question, not_applicable_text FROM template_questions WHERE template_name='client compliance guide'; --21 rows return

-- # have preparer answer with a mix that will show all complete

--then link and check links working by spreading y,n,na and blank in rotation for each template for the first checklist instance of each

--47 mixed answers for template 1; 21 for template 2
--checklist id shall be 1 or 2 and increment for each new checklist, so the next checlist will be 3 for as many rows as there are questions in the template
--answer_id will increment and not reset
--question_number will be 1 to 47 or 1 to 21 and will reset for each new checklist id based on the number of questions in teh template created
--role will be true for preparer, false for reviewer
--answer will be a string and either y,n,na or blank
--in our first block of two samples each checklist will cycle through response options and we will have an in progress set of checklists.
--in our second block of two samples (checklists 3 and 4) answers will all be y or na so the checklists can show as complete.
--in our third block we'll show a block of two checklists with no answers at all which will be a not started example set.

-- reviewer will be 1-6 cont autoincrement of answer_id but role will be false  after the 1-6 for preparer. Pretend the preparer's work is being reviewed in chunks.
-- # have reviewer answer with a mix showing incomplete which will produce Kanbans
-- # have reviewer answer with a mix that will show all complete - ready for recipient look


INSERT INTO answers (checklist_id, answer_id, question_number, role, answer)
VALUES
(1,1,1,true,'y'),
(1,2,2,true,'n'),
(1,3,3,true,'na'),
(1,4,4,true,''),
(1,5,5,true,'y'),
(1,6,6,true,'n'),
(1,7,7,true,'na'),
(1,8,8,true,''),
(1,9,9,true,'y'),
(1,10,10,true,'n'),
(1,11,11,true,'na'),
(1,12,12,true,''),
(1,13,13,true,'y'),
(1,14,14,true,'n'),
(1,15,15,true,'na'),
(1,16,16,true,''),
(1,17,17,true,'y'),
(1,18,18,true,'n'),
(1,19,19,true,'na'),
(1,20,20,true,''),
(1,21,21,true,'y'),
(1,22,22,true,'n'),
(1,23,23,true,'na'),
(1,24,24,true,''),
(1,25,25,true,'y'),
(1,26,26,true,'n'),
(1,27,27,true,'na'),
(1,28,28,true,''),
(1,29,29,true,'y'),
(1,30,30,true,'n'),
(1,31,31,true,'na'),
(1,32,32,true,''),
(1,33,33,true,'y'),
(1,34,34,true,'n'),
(1,35,35,true,'na'),
(1,36,36,true,''),
(1,37,37,true,'y'),
(1,38,38,true,'n'),
(1,39,39,true,'na'),
(1,40,40,true,''),
(1,41,41,true,'y'),
(1,42,42,true,'n'),
(1,43,43,true,'na'),
(1,44,44,true,''),
(1,45,45,true,'y'),
(1,46,46,true,'n'),
(1,47,47,true,'na'),
(2,48,1,true,''),
(2,49,2,true,'y'),
(2,50,3,true,'n'),
(2,51,4,true,'na'),
(2,52,5,true,''),
(2,53,6,true,'y'),
(2,54,7,true,'n'),
(2,55,8,true,'na'),
(2,56,9,true,''),
(2,57,10,true,'y'),
(2,58,11,true,'n'),
(2,59,12,true,'na'),
(2,60,13,true,''),
(2,61,14,true,'y'),
(2,62,15,true,'n'),
(2,63,16,true,'na'),
(2,64,17,true,'y'),
(2,65,18,true,'n'),
(2,66,19,true,'na'),
(2,67,20,true,''),
(2,68,21,true,'y'),
(3,69,1,true,'y'),
(3,70,2,true,'y'),
(3,71,3,true,'y'),
(3,72,4,true,'y'),
(3,73,5,true,'y'),
(3,74,6,true,'y'),
(3,75,7,true,'y'),
(3,76,8,true,'y'),
(3,77,9,true,'y'),
(3,78,10,true,'y'),
(3,79,11,true,'y'),
(3,80,12,true,'y'),
(3,81,13,true,'y'),
(3,82,14,true,'y'),
(3,83,15,true,'y'),
(3,84,16,true,'y'),
(3,85,17,true,'y'),
(3,86,18,true,'y'),
(3,87,19,true,'y'),
(3,88,20,true,'y'),
(3,89,21,true,'y'),
(3,90,22,true,'y'),
(3,91,23,true,'y'),
(3,92,24,true,'y'),
(3,93,25,true,'y'),
(3,94,26,true,'y'),
(3,95,27,true,'y'),
(3,96,28,true,'y'),
(3,97,29,true,'y'),
(3,98,30,true,'y'),
(3,99,31,true,'y'),
(3,100,32,true,'y'),
(3,101,33,true,'y'),
(3,102,34,true,'y'),
(3,103,35,true,'y'),
(3,104,36,true,'y'),
(3,105,37,true,'y'),
(3,106,38,true,'y'),
(3,107,39,true,'y'),
(3,108,40,true,'y'),
(3,109,41,true,'y'),
(3,110,42,true,'y'),
(3,111,43,true,'y'),
(3,112,44,true,'y'),
(3,113,45,true,'y'),
(3,114,46,true,'y'),
(3,115,47,true,'y'),
(4,116,1,true,'y'),
(4,117,2,true,'y'),
(4,118,3,true,'y'),
(4,119,4,true,'y'),
(4,120,5,true,'y'),
(4,121,6,true,'y'),
(4,122,7,true,'y'),
(4,123,8,true,'y'),
(4,124,9,true,'y'),
(4,125,10,true,'y'),
(4,126,11,true,'y'),
(4,127,12,true,'y'),
(4,128,13,true,'y'),
(4,129,14,true,'y'),
(4,130,15,true,'y'),
(4,131,16,true,'y'),
(4,132,17,true,'y'),
(4,133,18,true,'y'),
(4,134,19,true,'y'),
(4,135,20,true,'y'),
(4,136,21,true,'y'),
(5,137,1,true,''),
(5,138,2,true,''),
(5,139,3,true,''),
(5,140,4,true,''),
(5,141,5,true,''),
(5,142,6,true,''),
(5,143,7,true,''),
(5,144,8,true,''),
(5,145,9,true,''),
(5,146,10,true,''),
(5,147,11,true,''),
(5,148,12,true,''),
(5,149,13,true,''),
(5,150,14,true,''),
(5,151,15,true,''),
(5,152,16,true,''),
(5,153,17,true,''),
(5,154,18,true,''),
(5,155,19,true,''),
(5,156,20,true,''),
(5,157,21,true,''),
(5,158,22,true,''),
(5,159,23,true,''),
(5,160,24,true,''),
(5,161,25,true,''),
(5,162,26,true,''),
(5,163,27,true,''),
(5,164,28,true,''),
(5,165,29,true,''),
(5,166,30,true,''),
(5,167,31,true,''),
(5,168,32,true,''),
(5,169,33,true,''),
(5,170,34,true,''),
(5,171,35,true,''),
(5,172,36,true,''),
(5,173,37,true,''),
(5,174,38,true,''),
(5,175,39,true,''),
(5,176,40,true,''),
(5,177,41,true,''),
(5,178,42,true,''),
(5,179,43,true,''),
(5,180,44,true,''),
(5,181,45,true,''),
(5,182,46,true,''),
(5,183,47,true,''),
(6,184,1,true,''),
(6,185,2,true,''),
(6,186,3,true,''),
(6,187,4,true,''),
(6,188,5,true,''),
(6,189,6,true,''),
(6,190,7,true,''),
(6,191,8,true,''),
(6,192,9,true,''),
(6,193,10,true,''),
(6,194,11,true,''),
(6,195,12,true,''),
(6,196,13,true,''),
(6,197,14,true,''),
(6,198,15,true,''),
(6,199,16,true,''),
(6,200,17,true,''),
(6,201,18,true,''),
(6,202,19,true,''),
(6,203,20,true,''),
(6,204,21,true,'');

-- for Preparer
-- across all checklists
-- remember you can get out from END in terminal using \q

-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='y' AND role=true;  # link to template_questions yes_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='n' AND role=true;  # link to template_questions no_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='na' AND role=true; # link to template_questions not_applicable_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='' AND role=true; # link to template_questions question


-- and by checklist 1-6
--Checklist 1
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='y' AND role=true AND checklist_id=1;  # link to template_questions yes_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='n' AND role=true AND checklist_id=1;  # link to template_questions no_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='na' AND role=true AND checklist_id=1; # link to template_questions not_applicable_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='' AND role=true AND checklist_id=1; # link to template_questions question
--Checklist 2
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='y' AND role=true AND checklist_id=2;  # link to template_questions yes_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='n' AND role=true AND checklist_id=2;  # link to template_questions no_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='na' AND role=true AND checklist_id=2; # link to template_questions not_applicable_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='' AND role=true AND checklist_id=2; # link to template_questions question
--Checklist 3
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='y' AND role=true AND checklist_id=3;  # link to template_questions yes_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='n' AND role=true AND checklist_id=3;  # link to template_questions no_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='na' AND role=true AND checklist_id=3; # link to template_questions not_applicable_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='' AND role=true AND checklist_id=3; # link to template_questions question
--Checklist 4
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='y' AND role=true AND checklist_id=4;  # link to template_questions yes_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='n' AND role=true AND checklist_id=4;  # link to template_questions no_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='na' AND role=true AND checklist_id=4; # link to template_questions not_applicable_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='' AND role=true AND checklist_id=4; # link to template_questions question
--Checklist 5
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='y' AND role=true AND checklist_id=5;  # link to template_questions yes_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='n' AND role=true AND checklist_id=5;  # link to template_questions no_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='na' AND role=true AND checklist_id=5; # link to template_questions not_applicable_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='' AND role=true AND checklist_id=5; # link to template_questions question
--Checklist 6
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='y' AND role=true AND checklist_id=6;  # link to template_questions yes_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='n' AND role=true AND checklist_id=6;  # link to template_questions no_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='na' AND role=true AND checklist_id=6; # link to template_questions not_applicable_text
-- SELECT checklist_id, question_number, answer FROM answers WHERE answer='' AND role=true AND checklist_id=6; # link to template_questions question

--REVIEWER DATA

INSERT INTO answers (checklist_id, answer_id, question_number, role, answer)
VALUES
(1,205,1,false,'y'),
(1,206,2,false,'n'),
(1,207,3,false,'na'),
(1,208,4,false,''),
(1,209,5,false,'y'),
(1,210,6,false,'n'),
(1,211,7,false,'na'),
(1,212,8,false,''),
(1,213,9,false,'y'),
(1,214,10,false,'n'),
(1,215,11,false,'na'),
(1,216,12,false,''),
(1,217,13,false,'y'),
(1,218,14,false,'n'),
(1,219,15,false,'na'),
(1,220,16,false,''),
(1,221,17,false,'y'),
(1,222,18,false,'n'),
(1,223,19,false,'na'),
(1,224,20,false,''),
(1,225,21,false,'y'),
(1,226,22,false,'n'),
(1,227,23,false,'na'),
(1,228,24,false,''),
(1,229,25,false,'y'),
(1,230,26,false,'n'),
(1,231,27,false,'na'),
(1,232,28,false,''),
(1,233,29,false,'y'),
(1,234,30,false,'n'),
(1,235,31,false,'na'),
(1,236,32,false,''),
(1,237,33,false,'y'),
(1,238,34,false,'n'),
(1,239,35,false,'na'),
(1,240,36,false,''),
(1,241,37,false,'y'),
(1,242,38,false,'n'),
(1,243,39,false,'na'),
(1,244,40,false,''),
(1,245,41,false,'y'),
(1,246,42,false,'n'),
(1,247,43,false,'na'),
(1,248,44,false,''),
(1,249,45,false,'y'),
(1,250,46,false,'n'),
(1,251,47,false,'na'),
(2,252,1,false,''),
(2,253,2,false,'y'),
(2,254,3,false,'n'),
(2,255,4,false,'na'),
(2,256,5,false,''),
(2,257,6,false,'y'),
(2,258,7,false,'n'),
(2,259,8,false,'na'),
(2,260,9,false,''),
(2,261,10,false,'y'),
(2,262,11,false,'n'),
(2,263,12,false,'na'),
(2,264,13,false,''),
(2,265,14,false,'y'),
(2,266,15,false,'n'),
(2,267,16,false,'na'),
(2,268,17,false,'y'),
(2,269,18,false,'n'),
(2,270,19,false,'na'),
(2,271,20,false,''),
(2,272,21,false,'y'),
(3,273,1,false,'y'),
(3,274,2,false,'y'),
(3,275,3,false,'y'),
(3,276,4,false,'y'),
(3,277,5,false,'y'),
(3,278,6,false,'y'),
(3,279,7,false,'y'),
(3,280,8,false,'y'),
(3,281,9,false,'y'),
(3,282,10,false,'y'),
(3,283,11,false,'y'),
(3,284,12,false,'y'),
(3,285,13,false,'y'),
(3,286,14,false,'y'),
(3,287,15,false,'y'),
(3,288,16,false,'y'),
(3,289,17,false,'y'),
(3,290,18,false,'y'),
(3,291,19,false,'y'),
(3,292,20,false,'y'),
(3,293,21,false,'y'),
(3,294,22,false,'y'),
(3,295,23,false,'y'),
(3,296,24,false,'y'),
(3,297,25,false,'y'),
(3,298,26,false,'y'),
(3,299,27,false,'y'),
(3,300,28,false,'y'),
(3,301,29,false,'y'),
(3,302,30,false,'y'),
(3,303,31,false,'y'),
(3,304,32,false,'y'),
(3,305,33,false,'y'),
(3,306,34,false,'y'),
(3,307,35,false,'y'),
(3,308,36,false,'y'),
(3,309,37,false,'y'),
(3,310,38,false,'y'),
(3,311,39,false,'y'),
(3,312,40,false,'y'),
(3,313,41,false,'y'),
(3,314,42,false,'y'),
(3,315,43,false,'y'),
(3,316,44,false,'y'),
(3,317,45,false,'y'),
(3,318,46,false,'y'),
(3,319,47,false,'y'),
(4,320,1,false,'y'),
(4,321,2,false,'y'),
(4,322,3,false,'y'),
(4,323,4,false,'y'),
(4,324,5,false,'y'),
(4,325,6,false,'y'),
(4,326,7,false,'y'),
(4,327,8,false,'y'),
(4,328,9,false,'y'),
(4,329,10,false,'y'),
(4,330,11,false,'y'),
(4,331,12,false,'y'),
(4,332,13,false,'y'),
(4,333,14,false,'y'),
(4,334,15,false,'y'),
(4,335,16,false,'y'),
(4,336,17,false,'y'),
(4,337,18,false,'y'),
(4,338,19,false,'y'),
(4,339,20,false,'y'),
(4,340,21,false,'y'),
(5,341,1,false,''),
(5,342,2,false,''),
(5,343,3,false,''),
(5,344,4,false,''),
(5,345,5,false,''),
(5,346,6,false,''),
(5,347,7,false,''),
(5,348,8,false,''),
(5,349,9,false,''),
(5,350,10,false,''),
(5,351,11,false,''),
(5,352,12,false,''),
(5,353,13,false,''),
(5,354,14,false,''),
(5,355,15,false,''),
(5,356,16,false,''),
(5,357,17,false,''),
(5,358,18,false,''),
(5,359,19,false,''),
(5,360,20,false,''),
(5,361,21,false,''),
(5,362,22,false,''),
(5,363,23,false,''),
(5,364,24,false,''),
(5,365,25,false,''),
(5,366,26,false,''),
(5,367,27,false,''),
(5,368,28,false,''),
(5,369,29,false,''),
(5,370,30,false,''),
(5,371,31,false,''),
(5,372,32,false,''),
(5,373,33,false,''),
(5,374,34,false,''),
(5,375,35,false,''),
(5,376,36,false,''),
(5,377,37,false,''),
(5,378,38,false,''),
(5,379,39,false,''),
(5,380,40,false,''),
(5,381,41,false,''),
(5,382,42,false,''),
(5,383,43,false,''),
(5,384,44,false,''),
(5,385,45,false,''),
(5,386,46,false,''),
(5,387,47,false,''),
(6,388,1,false,''),
(6,389,2,false,''),
(6,390,3,false,''),
(6,391,4,false,''),
(6,392,5,false,''),
(6,393,6,false,''),
(6,394,7,false,''),
(6,395,8,false,''),
(6,396,9,false,''),
(6,397,10,false,''),
(6,398,11,false,''),
(6,399,12,false,''),
(6,400,13,false,''),
(6,401,14,false,''),
(6,402,15,false,''),
(6,403,16,false,''),
(6,404,17,false,''),
(6,405,18,false,''),
(6,406,19,false,''),
(6,407,20,false,''),
(6,408,21,false,'');
-- for reviewer

-- #SELECT answer FROM answers WHERE answer="y" # link to template_questions yes_text
-- #SELECT answer FROM answers WHERE answer="n" # link to template_questions no_text
-- #SELECT answer FROM answers WHERE answer="n/a"# link to template_questions not_applicable_text
-- #SELECT answer FROM answers WHERE answer=""# link to template_questions question

-- # 1.0 cont - button actions

-- # have preparer enter send to reviewer the 2 complete and mark one for return and one ready.

-- # have reviewer enter returned for corrections

-- # have reviewer enter sent to recipient


-- # 2.0
-- # query for returning Kanban lists, counts, percents - ready for review look
-- # reviewer Kanbans

-- # 3.0

-- # sql queries that will illustrate stats

-- # sql queries specifically on questions marked for review at any time

-- # once complete move on to convert to SQLAlchemy for web page display/ receipt of web input
