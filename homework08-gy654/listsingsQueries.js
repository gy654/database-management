// TODO: write MongoDB queries below

// mongoimport --headerline --type=csv --db=homework08 --collection=listings --file=listings.csv
// mongosh
// use homework08
// show collections

// 1. show exactly two documents from the listings collection in any order
db.listings.find().limit(2)

// 2. show exactly 10 documents in any order… but print in easier to read format and noting the host names for further use
db.listings.find().limit(10).pretty()

// 3. choose two host names… and show all of the listings hosted by either of the two hosts 
// (for example, "Kamilla" or "Sonder"… though these two names may not exist in the latest data set)
// only show the name, price, neighbourhood, and host_name
db.listings.find({host_name:{ $in: ['Jannifer', 'Ellis' ]}}, { name: 1, price: 1, neighbourhood: 1, host_name: 1 }).pretty()

// 4. find all of the unique host_name (see the docs)
db.listings.distinct('host_name')

// 5. find all of the places that have more than 2 beds in city (referred to as neighbourhood_group_cleansed in json file) Brooklyn, ordered by review_scores_rating descending
// only show the name, beds, city, review_scores_rating, and price
// if you run out of memory for this query, try filtering review_scores_rating that aren't empty ($ne)… and lastly, if there's still an issue, you can set beds to exactly 2
db.listings.find({'beds': {$gt: 2}, 'neighbourhood_group_cleansed': 'Brooklyn'}, {name: 1, beds: 1, city: 1, review_scores_rating: 1, price: 1}).sort({'review_scores_rating': -1 })

// 6. show the number of listings per host 
db.listings.aggregate([
    {$group: {_id: "$host_id", count: {$sum: 1}}}
])

// 7. in city (again, use neighbourhood_group_cleansed), Manhattan, 
// find the average review_scores_rating per neighbourhood, 
// and only show the ones above 4.5 if the scale if the scores is 0-5 or 95 if the scale of scores is 0-100… 
// sorted in descending order of rating (see the docs)


db.listings.aggregate([
    {$match: {neighbourhood_group_cleansed: "Manhattan"}},
    {$group: {_id: "$host_neighbourhood", average_rating: { $avg: "$review_scores_rating" }}},
    {$sort: {average_rating: -1}},
    {$match: {average_rating: { $gt: 4.5 }}}
  ])