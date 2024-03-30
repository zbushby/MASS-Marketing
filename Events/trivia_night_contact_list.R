# Project Trivia Night
library(dplyr)

# Read in csv files

Trivia_Night <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Granular Data//Attendence//trivia_night_attendence.csv")
wk3_members <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Newsletter//Data//Week 3 Tickets.csv")
tickets_info <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Granular Data//Attendence//ALL_Wk4.csv")

wk4_members <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Newsletter//Data//Week 4.csv")
#Events

flow <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Granular Data//Attendence//flow.csv")
first_games_night <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Granular Data//Attendence//First_Year_Games_Night.csv")
info_sesh <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Granular Data//Attendence//Info_Session.csv")
games_night <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Granular Data//Attendence//Games Night.csv")
#look at data

Trivia_Night %>% 
  select(First.Name, Last.Name, Email, Ticket.Type) %>% 
  head()


wk3_members %>% 
  select(First.name, Last.name, Email.address, Tickets) %>% 
  filter(Tickets != 0) %>% 
  head()

# MASS member + >=1 event attendence + arent going to trivia night
common_emails <- intersect(wk3_members$Email.address, Trivia_Night$Email)
wk3_members_filtered <- wk3_members[!wk3_members$Email.address %in% common_emails,]
wk3_members_filtered %>%
  select(First.name, Last.name, Email.address, Tickets) %>% 
  filter(Tickets != 0)

#this might be more useful ??
# >=1 event attendence + not going to trivia
common_emails_notmember <- intersect(tickets_info$Email, Trivia_Night$Email)
wk3_filtered <- tickets_info[!tickets_info$Email %in% common_emails_notmember,]
wk3_filtered

   #just getting first names
merged_df <- merge(wk3_filtered, wk3_members[, c("Email.address", "First.name", "Last.name")], by.x = "Email", by.y = "Email.address", all.x = TRUE)
#flow traders
flow_na_df <- merged_df[is.na(merged_df$First.name), ]
flow_non_na_df <- merged_df[!is.na(merged_df$First.name), ]
flow_na_df <- merge(flow_na_df[,c("Email", "Tickets")], flow[, c("Email", "First.name", "Last.name")], by.x = "Email", by.y = "Email", all.x = TRUE)
merged_df <- rbind(flow_non_na_df, flow_na_df)
#first_year_event
first_na_df <- merged_df[is.na(merged_df$First.name), ]
first_non_na_df <- merged_df[!is.na(merged_df$First.name), ]
first_na_df <- merge(first_na_df[,c("Email", "Tickets")], first_games_night[, c("Email", "First.name", "Last.name")], by.x = "Email", by.y = "Email", all.x = TRUE)
merged_df <- rbind(first_non_na_df, first_na_df)

#games night
gn_na_df <- merged_df[is.na(merged_df$First.name), ]
gn_non_na_df <- merged_df[!is.na(merged_df$First.name), ]
gn_na_df <- merge(gn_na_df[,c("Email", "Tickets")], games_night[, c("Email", "First.name", "Last.name")], by.x = "Email", by.y = "Email", all.x = TRUE)
merged_df <- rbind(gn_non_na_df, gn_na_df)

#info_sesh
info_na_df <- merged_df[is.na(merged_df$First.name), ]
info_non_na_df <- merged_df[!is.na(merged_df$First.name), ]
info_na_df <- merge(info_na_df[,c("Email", "Tickets", "Last.name")], info_sesh[, c("Email", "First.name")], by.x = "Email", by.y = "Email", all.x = TRUE)
merged_df <- rbind(info_non_na_df, info_na_df)

merged_df <- merged_df[, c("Email", "First.name", "Last.name", "Tickets")]

final_df <- merged_df %>% 
  mutate(Member = ifelse(Email %in% wk3_members$Email.address, "Yes", "No")) %>% 
  mutate(Flow_Traders = ifelse(Email %in% flow$Email, "Yes", "No")) %>%
  mutate(First_Year_GN = ifelse(Email %in% first_games_night$Email, "Yes", "No")) %>%
  mutate(Info_Sesh = ifelse(Email %in% info_sesh$Email, "Yes", "No")) %>%
  mutate(Games_Night = ifelse(Email %in% games_night$Email, "Yes", "No")) %>%
  unique() %>% 
  arrange(-Tickets, First.name)



write.csv(final_df, "//Users//zachbushby//Documents//edu//MASS//Data//Granular Data//Attendence//Trivia_Night_ContactList.csv", row.names = FALSE)









################################################################################

#people who havent bought membership but got the discount
wk4_members <- rename(wk4_members, Email = Email.address)

people_not_members <- anti_join(Trivia_Night, wk4_members, by = "Email") %>% 
  filter(Ticket.Type == "Club Member - Early Bird Sale") %>% 
  select(Email, First.Name, Last.Name)
  
people_not_members












