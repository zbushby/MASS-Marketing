
library(dplyr)

# Read the CSV files
wk3_tickets_info <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Granular Data//Attendence//ALL_Wk3.csv")
games_night <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Granular Data//Attendence//Games Night.csv")


# Combine the data frames and sum the tickets for each email
combined_df <- bind_rows(wk3_tickets_info, games_night) %>%
  group_by(Email) %>%
  summarise(Tickets = sum(Tickets, na.rm = TRUE))

# You can now write the combined data frame to a new CSV file if needed
write.csv(combined_df, "//Users//zachbushby//Documents//edu//MASS//Data//Granular Data//Attendence//ALL_Wk4.csv", row.names = FALSE)




##############################################################################
#Join Ticket Data onto membership base

#old members

# Read the CSV files
old_members <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Join Mass//Data//Filtered_Old_Members_MASS.csv")
tickets_info <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Granular Data//Attendence//ALL_Wk3.csv")

# Join the data frames, making sure to replace NA in Tickets with 0
final_df <- old_members %>%
  left_join(tickets_info, by = c("Email.address" = "Email")) %>%
  mutate(Tickets = ifelse(is.na(Tickets), 0, Tickets))

# Write the final data frame to a new CSV file
write.csv(final_df, "//Users//zachbushby//Documents//edu//MASS//Data//Join Mass//Data//Filtered_Old_Members_MASS_Tickets.csv", row.names = FALSE)



#2024 members


# Read the CSV files
old_members <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Newsletter//Data//Week 3.csv")
tickets_info <- read.csv("//Users//zachbushby//Documents//edu//MASS//Data//Granular Data//Attendence//ALL_Wk3.csv")

# Join the data frames, making sure to replace NA in Tickets with 0
final_df <- old_members %>%
  left_join(tickets_info, by = c("Email.address" = "Email")) %>%
  mutate(Tickets = ifelse(is.na(Tickets), 0, Tickets))

# Write the final data frame to a new CSV file
write.csv(final_df, "//Users//zachbushby//Documents//edu//MASS//Data//Newsletter//Data//Week 3 Tickets.csv", row.names = FALSE)


##############################################################################

